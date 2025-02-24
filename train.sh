#!/bin/bash

# Set dataset paths
export nnUNet_raw="/content/nnUNet_raw"
export nnUNet_preprocessed="/content/nnUNet_preprocessed"
export nnUNet_results="/content/drive/MyDrive/nnUNet_results"

# Train the model
# add --c if you want to continue the training
nnUNetv2_train 1 2d 0 --val_best
