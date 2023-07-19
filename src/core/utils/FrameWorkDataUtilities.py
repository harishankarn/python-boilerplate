import os
import shutil
from pathlib import Path
#from core.miniodb.utils import get_obj
import random
import numpy as np
import json
import sys
import os
import h5py
#import cv2
import logging
from core.utils.ModelUtilities import ModelUtilities 
from core.miniodb.MinioUtilities import MinioUtilities

class FrameWorkDataUtilities:
    logger=logging.getLogger(__name__)
    def __init__(self):  
        print("Logger", self.logger) 
        source_path = str(Path("./").resolve())
        sys.path.append(source_path)
     
    def copy_to_out(self,output_path,file,input_path=None):
        """
        copies save folder to output

        :param output_path: path for component output
        :return:
        """
        dir = os.path.dirname(os.path.realpath(file))
        folder = dir.split(".")[-1]
        save_path = f"{dir}/{folder}"

        Path(save_path).mkdir(parents=True, exist_ok=True)

        shutil.copytree(save_path,output_path+f'/{folder}',dirs_exist_ok=True)

        if input_path:
            shutil.copytree(input_path, output_path,dirs_exist_ok=True)


    def get_curr_dir(self,file):
        return os.path.dirname(os.path.realpath(file))

    def get_save_path(self,fn,file):
        """

        :param fn: filename
        :return: returns path for saving file
        """

        dir = os.path.dirname(os.path.realpath(file))
        folder = dir.split(".")[-1]

        save_path = f"{dir}/{folder}/{fn}"
        Path(save_path).parent.mkdir(parents=True, exist_ok=True)

        return save_path

    def get_npz(self,fn):
        return np.load(fn,allow_pickle=True)

    def load_file(self,fn,ext):

        if ext == 'npz':
            data = self.get_npz(fn)
            x, y = data['x'].reshape(1, -1), data['y']
            return x, y
        elif ext == 'hdf5':
            with h5py.File(fn, "r") as h:
                x, y = h['X'][:], h['Y'][:]
                return x, y
        else:
            return fn


    def data_generator(self,bucket,keys,ext='npz'):

        """
        A generator for the values of keys in the list

        :param bucket: corresponding minio bucket
        :param keys: corresponding keys
        :return: a generator
        """
        minioUtilities=MinioUtilities()
        while True:
            random.shuffle(keys)
            for key in keys:
                fn = minioUtilities.get_obj(bucket=bucket, key=key)
                x,y = self.load_file(fn,ext)
                yield x, y

    def mp4_2_array(self,fn,x1=400,x2=1400,y1=400,y2=1400,resize=(224,224)):
        """

        :param fn: filename of the mp4 file
        :param x1: x limit left
        :param x2: x limit right
        :param y1: y limit bottom
        :param y2: y limit top
        :param resize: required resize shape
        :return: array of frames
        """
        cap = cv2.VideoCapture(fn)
        ret, first_frame = cap.read()
        first_frame = first_frame[x1:x2, y1:y2, :]
        first_frame = cv2.resize(first_frame, resize, interpolation=cv2.INTER_NEAREST)

        IMG = [first_frame]

        while 1:
            ret, frame = cap.read()

            if ret:
                frame = frame[x1:x2, y1:y2, :]
                frame = cv2.resize(frame, resize, interpolation=cv2.INTER_NEAREST)

                IMG.append(frame)
            else:
                break

        return np.array(IMG)