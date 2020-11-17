import io
from Symbol import *
from tkinter import *
from tkinter.ttk import *
import os
# import tensorflow as tf





if __name__ == "__main__":
    training_data_path = "/Users/ivy/Desktop/Senior_Seminar/manuscript/training-data"
    output_images_dir = "/Users/ivy/Desktop/Senior_Seminar/Uhh/HOMUS_directory_structure"
    filepaths = [os.path.join(dp, f) for dp, dn, filenames in os.walk(training_data_path) for f in filenames if os.path.splitext(f)[1] == '.txt']

    symbols_list = list(map((lambda n: Symbol(n)), filepaths))
    # print(symbols_list)
    for symbol in symbols_list:
        directory_to_write=f"{output_images_dir}/{symbol.name}/{symbol.filename}"
        print(f"Writing to: {directory_to_write}")
        symbol.draw(directory_to_write)
    
    # print(symbols_list)