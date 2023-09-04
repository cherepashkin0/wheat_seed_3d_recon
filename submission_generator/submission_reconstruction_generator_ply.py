import os
from pathlib import Path
from helpers import create_zip_archive
from submission_reconstruction_generator_npy import recon_generation
cur_dir = os.getcwd()


def main():
    """generate random submission"""
    predicted_recon_points_test, order_dict = recon_generation(cur_dir)
    save_zip_ply(predicted_recon_points_test, order_dict)


def save_zip_ply(predicted_recon_points_test, order_dict):
    Path(os.path.join(cur_dir, 'submission/reconstruction')).mkdir(parents=True,
                                                                   exist_ok=True)
    for rel_idx, abs_idx in enumerate(order_dict['test']):
        with open(os.path.join(cur_dir, 'submission/reconstruction/{}.ply'.format(str(abs_idx).zfill(4))), 'w') as f:
            write_ply(f, predicted_recon_points_test[rel_idx].T)
    create_zip_archive([os.path.join(cur_dir, 'submission/reconstruction/test_submission.csv')] +
                        [os.path.join(cur_dir, 'submission/reconstruction/{}.ply'.format(str(abs_idx).zfill(4)))\
                         for abs_idx in order_dict['test']],
                       ['test_submission.csv'] +\
                       [os.path.join('{}.ply'.format(str(abs_idx).zfill(4))) for abs_idx in order_dict['test']],
                       os.path.join(cur_dir, 'submission/reconstruction_ply.zip'))
    print('submission file was saved to {}'.format(os.path.join(cur_dir, 'submission/reconstruction_ply.zip')))


def write_ply_header(file, num_vertices):
    header = (
        "ply\n"
        "format ascii 1.0\n"
        "element vertex {}\n"
        "property float x\n"
        "property float y\n"
        "property float z\n"
        "end_header\n"
    ).format(num_vertices)

    file.write(header)


def write_ply(file, vertices):
    num_vertices = vertices.shape[0]
    write_ply_header(file, num_vertices)
    for i in range(num_vertices):
        x, y, z = vertices[i]
        file.write(f"{x:.4f} {y:.4f} {z:.4f}\n")


if __name__ == '__main__':
    main()