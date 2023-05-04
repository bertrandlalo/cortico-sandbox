import mne
import numpy as np
import pandas as pd
import json


def make_raw(
    signal: pd.DataFrame, events: pd.DataFrame, rate: float, fname: str
) -> mne.io.RawArray:
    # Create mne object
    channels = list(signal.columns.values)
    info = mne.create_info(ch_names=channels, sfreq=rate, ch_types="eeg")
    info.set_montage("standard_1020")

    # Extract signal
    recording_times = signal.index.values.astype(np.int64) * 1e-9
    data = signal.values.T * 1e-6

    raw = mne.io.RawArray(data, info)
    raw._filenames = [fname]
    raw.set_meas_date(recording_times[0])

    # Extract annotations
    flashes = events.loc[events["label"] == "flash_begins"]
    onsets = flashes.index.values.astype(np.int64) * 1e-9
    groups = []
    labels = []
    for meta in flashes["data"]:
        meta = json.loads(meta)
        groups.append(meta["group"])
        if meta["includes_target"] == True:
            label = "target"
        elif meta["includes_target"] == False:
            label = "non-target"
        else:
            label = "unknown"
        labels.append(label)
    annotations = mne.Annotations(onsets, 0, labels, orig_time=0)

    raw.set_annotations(annotations)
    annotations
    return raw
