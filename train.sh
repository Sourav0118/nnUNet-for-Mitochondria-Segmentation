#!/bin/bash
# Clone nnUNet repository
git clone https://github.com/MIC-DKFZ/nnUNet.git
cd nnUNet
pip install -e .

# Set dataset paths
export nnUNet_raw="/content/nnUNet_raw"
export nnUNet_preprocessed="/content/nnUNet_preprocessed"
export nnUNet_results="/content/drive/MyDrive/nnUNet_results"

# Preprocess dataset
nnUNetv2_plan_and_preprocess -d 1 --verify_dataset_integrity

# Train the model
# add --c if you want to continue the training
nnUNetv2_train 1 2d 0 --val_best
