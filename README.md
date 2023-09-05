Submission examples for Wheat Seed 3d Reconstruction Challenge 
===
1. Install python 3, pandas, numpy.  
2. To create submission file for **track #1** "Volume Regression", run the command `python submission_generator/submission_volume_generator.py`     
3. To create submission files for **track #2** "3D Reconstruction" with numpy file, run the command `python submission_generator/submission_reconstruction_generator_npy.py`
4. To create submission files for **track #2** "3D Reconstruction" with ply files, run the command `python submission_generator/submission_reconstruction_generator_ply.py`

This will generate submission with random numbers: `submission/volume_regression.zip` for **track #1**, `submission/reconstructoin_npy.zip` or`submission/reconstructoin_ply.zip` for **track #2**. To generate a submission with actual values, replace the random number generation lines with lines that load the predicted values of your model. 