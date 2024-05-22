# Path: dataset.py
import os

# The dataset class was written in Python and used PyTorch (Paszke et al., 2017) to load the fish images and their corresponding measurements.
# The dataset class was used to load the images and measurements from the training data.
# The images were resized to 200 pixels by 75 pixels and normalized to have pixel values between 0 and 1.
# The measurements were normalized to have values between 0 and 1.
# The dataset class was used to create data loaders for training and validation.

import torch
import cv2
import numpy as np

class FishDataset(torch.utils.data.Dataset):

    def __init__(self):
        self.data = []
        self.labels = []

        # Load the data
        #标签存储在fish_label文件夹中，以txt文件存储，每一个txt文件里只有一行，为一个图片的标签，格式为x1,y1,x2,y2,specie,length
        #图片存储在fish_images文件夹中，以jpg格式存储
        #标签与图片根据文件名对应

        # Load the data
        for file in os.listdir('fish_label'):
            with open(os.path.join('fish_label', file), 'r') as f:
                label = f.read().strip().split(',')
                label = [float(x) for x in label]
                self.labels.append(label)

        for file in os.listdir('fish_images'):
            image = cv2.imread(os.path.join('fish_images', file))
            #os.path.join('fish_images', file)的
            image = cv2.resize(image, (200, 75))
            image = image.transpose((2, 0, 1))
            image = image.astype(np.float32)
            image /= 255.0
            self.data.append(image)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        image = self.data[idx]
        label = self.labels[idx]
        return torch.from_numpy(image), torch.tensor(label)
