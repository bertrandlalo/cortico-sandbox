# cortico-sandbox
Playground repository for Cortico Masterclass on Open Science and reproducibility. 

## Context
Visualization of P300 data acquired with HackEEG and Timeflux.

## Code 
### Prerequisites

- Git
- Python > 3.8
- Miniconda or Anaconda  
- Jupyter 

### Clone the repo

```
git clone https://github.com/bertrandlalo/cortico-sandbox
```

### Install 

```
> conda create --name cortico-sandbox python=3.10 pytables
> conda activate cortico-sandbox
> pip install -r requirements.txt
```

### Data
One dataset can be found in `/data`.
It was acquired using: 
- [HackEEG device](https://www.starcat.io/shop/hackeeg/);
- [Timeflux HackEEG driver](https://github.com/timeflux/timeflux_hackeeg);
- [Timeflux P300 Speller](https://github.com/timeflux/demos/tree/main/speller/P300)


### Notebooks

- Offline: 
  - Read data from HDF5
  - Convert into a MNE object
  - Bandpass + Notch
  - Visualize the ERPs

- Online:
  - Read data from HDF5
  - Execute the timeflux graph offline (as a branch)
  - Visualize the ERPs

## Contribute / Hands on

This repo is meant to be a playground, to experiment Github.
For example, you can practice by: 
- opening some issues
- forking the repository to your own organization
- opening a Pull Request 
- reviewing a Pull Request 
