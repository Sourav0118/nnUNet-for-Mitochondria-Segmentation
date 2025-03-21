# Mitochondria segmentation from Electron Microscopy Images using nn-UNet

## Overview
This repository provides a pipeline for symantic segmentation of mitochondria from Electron Microscopy Images using nn-UNet. The dataset used can be downloaded from [here](https://www.epfl.ch/labs/cvlab/data/data-em/) It also includes scripts for training, inference, and evaluation of nnUNet models using Jaccard Index and Dice Score metrics.

### Official implementation of nn-UNet: [Link](https://github.com/MIC-DKFZ/nnUNet)

## Dataset Structure
Ensure your dataset follows the nnUNet format:
```
/Dataset001_mitochondria/
│── imagesTr/          # Training images
│── imagesTs/          # Test images
│── labelsTr/          # Training labels
│── labelsTs/          # Test labels
│── dataset.json       # Dataset configuration
```

## Installation
Clone the nnUNet repository and install dependencies:
```bash
!git clone https://github.com/MIC-DKFZ/nnUNet.git
cd nnUNet
!pip install -e .
```

## Convert TIFF to NIfTI
Run the conversion script:
```bash
python tiff_to_nifti.py --input /path/to/tiff --output /content/nnUNet_raw/Dataset001_mitochondria
```
Ensure `dataset.json` is included in the dataset folder. The dataset.json is provided in the repo.

## Preprocessing
```bash
bash preprocess.sh
```

## Training
```bash
bash train.sh
```

## Inference
```bash
bash inference.sh
```

## Evaluation
Run the evaluation script to compute Jaccard Index and Dice Score:
```bash
python evaluation.py
```

## Checkpoints
Give the shared nnUNet_results folder as the path to nnUNet_results. [nnUNet_results](https://drive.google.com/drive/folders/1PfeXNPlkOSEQuZuT8qmWDTMoTOdO_96y?usp=drive_link). This folder contains the checkpoints and the rest of the training details along with log files. 

## Results
| Metric              | Score  |
|--------------------|--------|
| Dice Score        | 0.86   |
| Jaccard Index (IoU) | 0.92   |
