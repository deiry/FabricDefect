from PIL import Image
import requests
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import csv
from skimage.io import imread



def download_data():
    cwd = os.getcwd()
    with open("img_ids.csv", 'r') as f:
        list_id = list(csv.reader(f, delimiter="\n"))

    img_ids = np.array(list_id)
    img_ids = img_ids.reshape(500,)
    url = 'https://github.com/deiry/20191.DL/blob/proyect/Proyect/data/'
    url2 = '?raw=true'
    folder = cwd + "/data/"
    for img_id in img_ids:
     
        path = url + img_id + url2
    
        im = Image.open(requests.get(path, stream=True).raw)
        im = im.resize((100, 100))
        plt.imshow(im)
        path_file = folder+img_id
        im.save(path_file)
   
    return img_ids


def get_data_numpy(limit=500):
    cwd = os.getcwd()
    data = []
    folder = cwd + "/data/"
    img_ids = next(os.walk(folder))[2]
    img_ids = img_ids[0:limit]
    for n, id_ in enumerate(img_ids):
        path = PATH + id_
        img = imread(path)
        img = resize(img, (28,28))
        data.append(img)
    data_np = np.array(data)
    return data_np


def save_data_numpy():
    with open("img_ids.csv", 'r') as f:
        list_id = list(csv.reader(f, delimiter="\n"))

    img_ids = np.array(list_id)
    img_ids = img_ids.reshape(500,)


    #img_ids = img_ids[0:limit]

    data = []
    cwd = os.getcwd()
    path = cwd +'/data/'

    for id_ in (img_ids):
        path = PATH + id_
        img = imread(path)

        np.save(cwd+'/dataset/'+id_, img)

        data.append(img)
    

