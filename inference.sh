#!/bin/bash
# Set paths
export nnUNet_raw="/content/nnUNet_raw"
export nnUNet_preprocessed="/content/nnUNet_preprocessed"
export nnUNet_results="/content/drive/MyDrive/nnUNet_results"

# Run inference
nnUNet_predict -i /content/nnUNet_raw/Dataset001_mitochondria/imagesTs \
-o /content/nnUNet_raw/Dataset001_mitochondria/predictionTs \
-d 1 -c 2d -f 0 -chk checkpoint_best.pth
