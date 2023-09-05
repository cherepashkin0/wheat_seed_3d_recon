Submission examples for Wheat Seed 3d Reconstruction Challenge 
===
1. Install python 3, pandas, numpy.  
2. To create submission file for **track #1** "Volume Regression", run the command `python submission_generator/submission_volume_generator.py`     
3. To create submission files for **track #2** "3D Reconstruction" with numpy file, run the command `python submission_generator/submission_reconstruction_generator_npy.py`
4. To create submission files for **track #2** "3D Reconstruction" with ply files, run the command `python submission_generator/submission_reconstruction_generator_ply.py`

This will generate submission with random numbers: `submission/volume_regression.zip` for **track #1**, `submission/reconstructoin_npy.zip` (or`submission/reconstructoin_ply.zip`) for **track #2**. To generate a submission with actual values, replace the random number generation lines with lines that load the predicted values of your model. 

For the **track #1** it must be 2964 values (2520 for train set and 444 for test set). For the **track #2** it must be 2964x2000  - per seed the model should produce 2000 length values of the radius vectors, lying on the corresponding directions. Provided script `submission_reconstruction_generator_npy.py` (or `submission_reconstruction_generator_ply.py`) convert these lengths into 3d point cloud and [calculate volume](https://github.com/cherepashkin0/wheat_seed_3d_recon/blob/main/submission_generator/submission_reconstruction_generator_npy.py#L-CustomVolumeCalculationProcedure)
