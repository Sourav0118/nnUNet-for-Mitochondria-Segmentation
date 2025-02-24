import os
import numpy as np
import tifffile as tiff
import nibabel as nib
import argparse
from tqdm import tqdm

def convert_tiff_to_nnunet(image_tiff_path, label_tiff_path, output_dir, img_sub_folder, lb_sub_folder, dataset_name="Dataset001_mitochondria"):
    """
    Convert stacked TIFF images and segmentation masks to nnU-Net dataset structure.
    
    Parameters:
    - image_tiff_path (str): Path to the stacked TIFF file containing input images.
    - label_tiff_path (str): Path to the stacked TIFF file containing segmentation masks.
    - output_dir (str): Path to the nnU-Net dataset root.
    - dataset_name (str): Name of the dataset directory.
    """
    
    # Load the stacked TIFF files
    images = tiff.imread(image_tiff_path)  # Shape: (N, H, W)
    labels = tiff.imread(label_tiff_path)  # Shape: (N, H, W)

    # Validate dimensions
    assert images.shape == labels.shape, "Error: Image and Label TIFF stacks must have the same shape!"
    
    # Define nnU-Net paths
    dataset_path = os.path.join(output_dir, dataset_name)
    imagesTr_path = os.path.join(dataset_path, img_sub_folder)
    # imagesTs_path = os.path.join(dataset_path, "imagesTs")
    labelsTr_path = os.path.join(dataset_path, lb_sub_folder)
    os.makedirs(imagesTr_path, exist_ok=True)
    # os.makedirs(imagesTs_path, exist_ok=True)
    os.makedirs(labelsTr_path, exist_ok=True)

    num_slices = images.shape[0]

    print(f"Processing {num_slices} slices...")

    # Convert each slice into a .nii.gz file
    for i in tqdm(range(num_slices)):
        image_slice = images[i].astype(np.float32)  # Convert image to float32
        label_slice = (labels[i]>0).astype(np.int8)    # Convert label to uint8 (binary mask)
        # print(label_slice)
        # break

        # Save as NIfTI files
        img_nifti = nib.Nifti1Image(image_slice, affine=np.eye(4))
        lbl_nifti = nib.Nifti1Image(label_slice, affine=np.eye(4))

        idx = i #+ 165
        img_filename = os.path.join(imagesTr_path, f"case_{idx:03d}_0000.nii.gz")
        lbl_filename = os.path.join(labelsTr_path, f"case_{idx:03d}.nii.gz")

        nib.save(img_nifti, img_filename)
        nib.save(lbl_nifti, lbl_filename)

    print("Conversion completed successfully.")

    print(f"Dataset structure created at {dataset_path}")
