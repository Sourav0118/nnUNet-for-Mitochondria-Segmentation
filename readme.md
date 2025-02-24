# Mitochondria segmentation from Electron Microscopy Images using nn-UNet

## Overview
This repository provides a pipeline for instance segmentation of mitochondria from Electron Microscopy Images using nn-UNet. The dataset used can be downloaded from [here](https://www.epfl.ch/labs/cvlab/data/data-em/) It also includes scripts for training, inference, and evaluation of nnUNet models using Jaccard Index and Dice Score metrics.

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
!nnUNet_raw="/content/nnUNet_raw" nnUNet_preprocessed="/content/nnUNet_preprocessed" nnUNet_results="/content/drive/MyDrive/nnUNet_results" nnUNetv2_plan_and_preprocess -d 1 --verify_dataset_integrity
```

## Training
```bash
!nnUNet_raw="/content/nnUNet_raw" nnUNet_preprocessed="/content/nnUNet_preprocessed" nnUNet_results="/content/drive/MyDrive/nnUNet_results" nnUNetv2_train 1 2d 0 --val_best --c
```

## Inference
```bash
!nnUNet_raw="/content/nnUNet_raw" nnUNet_preprocessed="/content/nnUNet_preprocessed" nnUNet_results="/content/drive/MyDrive/nnUNet_results" nnUNet_predict -i /content/nnUNet_raw/Dataset001_mitochondria/imagesTs -o /content/nnUNet_raw/Dataset001_mitochondria/predictionTs -d 1 -c 2d -f 0 -chk checkpoint_best.pth
```

## Evaluation
Run the evaluation script to compute Jaccard Index and Dice Score:
```bash
python evaluation.py
```

## Checkpoints
Download pretrained model checkpoints from [this link](YOUR_CHECKPOINT_LINK_HERE).

## Results
| Metric              | Score  |
|--------------------|--------|
| Dice Score        | 0.86   |
| Jaccard Index (IoU) | 0.92   |
