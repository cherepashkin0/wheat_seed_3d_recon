import os
import pandas as pd
import numpy as np
from pathlib import Path
from helpers import create_zip_archive, perform_correction, load_order_dict
import datetime
cur_dir = os.getcwd()


def main():
    """generate random submission"""
    df = pd.DataFrame()
    order_dict = load_order_dict(cur_dir)
    # substitute with your own volume regression
    predicted_volume = {'train': np.random.uniform(5, 60, 2520),
                        'test': np.random.uniform(5, 60, 444)}
    gt_volume = pd.read_csv(os.path.join(cur_dir, 'general_files/train_gt_volumes.csv'))['volume'].values
    corrected_volume = perform_correction(predicted_volume, gt_volume)
    df['index'] = order_dict['test'].astype(int)
    df['volume'] = corrected_volume
    Path(os.path.join(cur_dir, 'submission/volume_regression')).mkdir(parents=True, exist_ok=True)
    df.to_csv(os.path.join(cur_dir, 'submission/volume_regression/test_submission.csv'), index=False)
    create_zip_archive([os.path.join(cur_dir, 'submission/volume_regression/test_submission.csv')],
                       ['test_submission.csv'], os.path.join(cur_dir, 'submission/volume_regression.zip'))
    print('submission file was saved to {}'.format(os.path.join(cur_dir, 'submission/volume_regression.zip')))


if __name__ == '__main__':
    main()