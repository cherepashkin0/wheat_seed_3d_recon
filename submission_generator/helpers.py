import os
import zipfile
import numpy as np

def create_zip_archive(input_pathes, input_names, output_zip_path):
    """create zip archive from files with input_pathes, with names input_names, to file output_zip_path"""
    if os.path.exists(output_zip_path):
        os.remove(output_zip_path)
    with zipfile.ZipFile(output_zip_path, 'w') as zf:
        for input_path, input_name in zip(input_pathes, input_names):
            zf.write(input_path, arcname=input_name)


def perform_correction(predicted_volume, gt_volume):
    """correction on bias using gt volume of the train set"""
    slope, intercept = np.polyfit(predicted_volume['train'], gt_volume, 1)
    corrected_volume = slope * predicted_volume['test'] + intercept
    return corrected_volume


def read_indices_from_file(file_path):
    """read indices from file, empty lines are ignored"""
    with open(file_path, "r") as f:
        lines = f.readlines()
    return np.array([int(line.strip()) for line in lines])


def load_order_dict(cur_dir):
    """load indices for train and test sets"""
    order_dict = {}
    file_mapping = {
        "train": "indices_train.txt",
        "test": "indices_test.txt"
    }

    for key, file_name in file_mapping.items():
        file_path = os.path.join(cur_dir, f'general_files/{file_name}')
        order_dict[key] = read_indices_from_file(file_path)

    return order_dict