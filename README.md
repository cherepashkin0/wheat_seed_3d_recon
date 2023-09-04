wheat_seed_3d_recon
===
# Submission generation
1. Install python 3, pandas, numpy.  
2. To create submission file for track #1 "volume regression", run the command `python submission_generator/submission_volume_generator.py`     
3. To create submission files for track #2 "reconstruction" with numpy file, run the command `python submission_generator/submission_reconstruction_generator_npy.py`
4. To create submission files for track #2 "reconstruction" with ply files, run the command `python submission_generator/submission_reconstruction_generator_ply.py`

This will generate submission with random numbers. To generate submission with actual values, substitute corresponding lines with values from your model prediction. 