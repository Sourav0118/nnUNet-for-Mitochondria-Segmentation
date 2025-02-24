export nnUNet_raw="/content/nnUNet_raw"
export nnUNet_preprocessed="/content/nnUNet_preprocessed"
export nnUNet_results="/content/drive/MyDrive/nnUNet_results"

# Run preprocess and verification of dataset integrity
nnUNetv2_plan_and_preprocess -d 1 --verify_dataset_integrity
