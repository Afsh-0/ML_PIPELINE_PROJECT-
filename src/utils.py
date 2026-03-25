from src.logger import logging
from src.exception import CustmeException
import os, sys
import pickle

"""now we will define a function to save a pkl file and inside it first we will define a path and second call an object and in next 
stage will will define a path as dir_path and later we will create a dir of that path and after that we will open it in wb mode which 
is write mode and dump a pickle file there in obj from file_obj"""
def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustmeException(e, sys)

#now go to data_transformation.py to save pkl in file

