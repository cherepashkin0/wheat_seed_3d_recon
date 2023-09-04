import os
import pandas as pd
import numpy as np
from pathlib import Path
from helpers import create_zip_archive, perform_correction, load_order_dict
cur_dir = os.getcwd()


def main():
    """generate random submission"""
    df = pd.DataFrame()
    order_dict = load_order_dict(cur_dir)
    # substitute with your own reconstruction
    predicted_recon_f = {'train': np.random.uniform(0, 3.5, (2520, 2000)),
                        'test': np.random.uniform(0, 3.5, (444, 2000))}
    directions = pd.read_csv(os.path.join(cur_dir, 'general_files/directions.csv'))
    with open(os.path.join(cur_dir, 'general_files/triangles.txt'), "r") as f:
        lines = f.readlines()
    triangles = np.array([[int(line.strip().split(' ')[i]) for i in range(3)] for line in lines if line]).reshape(-1, 3)
    directions_array = directions[['azimuth', 'elevation']].values.T
    predicted_recon_points_train = f2points(predicted_recon_f['train'], directions_array)
    predicted_recon_points_test = f2points(predicted_recon_f['test'], directions_array)
    volume_pred_train = points_to_volume(predicted_recon_points_train, triangles)
    volume_pred_test = points_to_volume(predicted_recon_points_test, triangles)
    gt_volume = pd.read_csv(os.path.join(cur_dir, 'general_files/train_gt_volumes.csv'))['volume'].values
    predicted_volume = {'train': volume_pred_train,
                        'test': volume_pred_test}
    corrected_volume = perform_correction(predicted_volume, gt_volume)
    df['index'] = order_dict['test'].astype(int)
    df['volume'] = corrected_volume
    Path(os.path.join(cur_dir, 'submission/reconstruction')).mkdir(parents=True, exist_ok=True)

    df.to_csv(os.path.join(cur_dir, 'submission/reconstruction/test_submission.csv'), index=False)
    np.save(os.path.join(cur_dir, 'submission/reconstruction/test_submission.npy'), predicted_recon_points_test.astype(np.float32))
    create_zip_archive([os.path.join(cur_dir, 'submission/reconstruction/test_submission.csv'),
                        os.path.join(cur_dir, 'submission/reconstruction/test_submission.npy')],
                        ['test_submission.csv', 'test_submission.npy'], os.path.join(cur_dir, 'submission/reconstruction.zip'))
    print('submission file was saved to {}'.format(os.path.join(cur_dir, 'submission/reconstruction.zip')))



def f2points(arr, dirs):
    """converts f values to points"""
    points = np.einsum('ij,jk->ikj', arr,
              np.stack([np.cos(dirs[0]) * np.sin(dirs[1]), np.sin(dirs[0]) * np.sin(dirs[1]), np.cos(dirs[1])],
                       axis=-1))
    return points


def points_to_volume(points, triangles):
    """calculate volume for each point cloud in points"""
    volume_pred = np.full(len(points), np.nan)
    for bs_idx in range(points.shape[0]):
        matr_a = points[bs_idx, :, triangles]  # current vertices of the prediction
        volume_pred[bs_idx] = (1/6) * np.sum(np.linalg.det(matr_a))
    return volume_pred


if __name__ == '__main__':
    main()