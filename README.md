# What is this for?

This project is for turning the HOMUS project into bitmap images. Previously, the HOMUS project was only stored in vector image files in a strange format that required writing custom software to open. In order to run ML on it, I had to convert it into a more accessible format. To do so, I forked my previous work on the Manuscript project to create a HOMUS to PNG generator.

## Usage

In order to use this program, first create an empty top level directory. Next, create a directory for each class of symbols within this directory. Name these the **EXACTLY** as they are named in the HOMUS files. 

Set the top level directory as the `output_images_dir` in `bitmapifier.py`. 

Next, point the program to an unzipped version of the HOMUS dataset. Set the path of the dataset to the `training_data_path` variable. 

Run `python3 bitmapifier.py`, and it should output the png files into the output directory. If the program crashes, then you named one of the class directories wrong. Make sure it exactly matches the line that the program outputted before it crashed. 