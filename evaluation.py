import os
import numpy as np
import nibabel as nib
from sklearn.metrics import jaccard_score

def dice_coefficient(y_true, y_pred):
    intersection = np.sum(y_true * y_pred)
    return (2. * intersection) / (np.sum(y_true) + np.sum(y_pred))

def jaccard_index(y_true, y_pred):
    return jaccard_score(y_true.flatten(), y_pred.flatten())

# Paths
ground_truth_dir = "/content/nnUNet_raw/Dataset001_mitochondria/labelsTs"
predictions_dir = "/content/nnUNet_raw/Dataset001_mitochondria/predictionTs"

# Compute evaluation metrics
iou_scores = []
dice_scores = []

for case in os.listdir(ground_truth_dir):
    gt_path = os.path.join(ground_truth_dir, case)
    pred_path = os.path.join(predictions_dir, case)

    gt = nib.load(gt_path).get_fdata() > 0  # Binarize
    pred = nib.load(pred_path).get_fdata() > 0  # Binarize

    iou = jaccard_index(gt, pred)
    dice = dice_coefficient(gt, pred)

    iou_scores.append(iou)
    dice_scores.append(dice)

print(f"Mean Jaccard Index (IoU): {np.mean(iou_scores)}")
print(f"Mean Dice Score (DSC): {np.mean(dice_scores)}")
