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
        limit = 50
        self.max_length = 0
        self.pos = []
        self.name = []
        self.num_in_pic = []
        print('Loading data...')
        # Load the data
        # 标签存储在fish_label文件夹中，以txt文件存储，每一个txt文件里只有一行，为一个图片的标签，格式为x1,y1,x2,y2,specie,length
        # 图片存储在fish_images文件夹中，以jpg格式存储
        # 标签与图片根据文件名对应

        # Load the data
        path = 'fish_tray_labels'
        # 读取txt文件中的标签.
        # 文件中有多行，每一行代表一个图片的标签，格式为x1,y1,x2,y2,specie,length
        # 将一个文件中的标签存储在一个list中，然后将这个list存储在self.labels中
        i = 0
        for file in os.listdir(path):
            self.name.append(file)
            print(file)
            with open(os.path.join(path, file)) as f:
                all_data = f.readlines()
                if len(all_data) > self.max_length:
                    self.max_length = len(all_data)
                single_label = []
                j = 0
                for data in all_data:

                    if data == '\n':
                        continue
                    data = data.split(',')
                    data = [float(x) for x in data]
                    self.pos.append(data[:4])
                    # single_label.append(data)
                    # print(data)
                    self.labels.append(data[4:])
                    j += 1
            self.num_in_pic.append(j)
            i += 1
            if i == limit:
                break
        print('Loaded', len(self.num_in_pic), 'labels.')
        print('max_length:', self.max_length)



                # data = f.read()
                # data = data.split(',')
                # data = [float(x) for x in data]
                # self.labels.append(data)

        # Load the images
        path = 'fish_tray_images'
        path_list = os.listdir(path)
        # path_list.remove('.DS_Store')
        path_list.sort(key=lambda x: int(x.split('_')[0]))

        i = 0
        for file in os.listdir(path):
            # print(file)
            # 不考虑后缀名,只考虑文件名,比较文件名是否相同
            if (len(self.num_in_pic) <= i) or (self.remove_suffix(file) != self.remove_suffix(self.name[i])) :
                continue

            print(file)

            # if file.split('.')[0] != self.name[i].split('.')[0]:
            #     continue

            image = cv2.imread(os.path.join(path, file))

            # 按照图片对应的标签里的xy坐标，，并将其他部分填充为0。使用遍历，注意每张图片的遍历次数为self.num_in_pic[i]
            # 将裁剪后的图片存储在self.data中

            for j in range(self.num_in_pic[i]):
                image_temp = image

                x1, y1, x2, y2 = self.pos[j]
                # 转成int类型
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                # print(x1, y1, x2, y2)

                # 把图片按照相应的坐标裁剪，并保持其大小不变，并将其他部分填充为0
                image_temp = cv2.resize(image_temp, (200, 75))

                if(x1>x2):
                    t=x1
                    x1=x2
                    x2=t
                if(y1>y2):
                    t=y1
                    y1=y2
                    y2=t


                image_temp = image_temp[y1:y2, x1:x2]
                image_temp = cv2.copyMakeBorder(image_temp, y1, 75 - y2, x1, 200 - x2, cv2.BORDER_CONSTANT, value=[255, 255, 255])

                image_temp = image_temp.transpose((2, 0, 1))
                image_temp = image_temp.astype(np.float32)
                image_temp /= 255.0

                image_temp = image_temp.tolist()
                self.data.append(image_temp)

            # os.path.join('fish_images', file)的
            # image = cv2.resize(image, (200, 75))
            # image = image.transpose((2, 0, 1))
            # image = image.astype(np.float32)
            # image /= 255.0
            # print('Loading image', i)
            # image = image.tolist()
            # self.data.append(image)
            i += 1
            if i == limit:
                break
        print('Loaded', i, 'images.')

    def remove_suffix(self,s):
        return s[:s.rfind('.')]
    def __len__(self):
        return len(self.data)


    def __getitem__(self, idx):
        image = self.data[idx]
        label = self.labels[idx]

        # Pad the label if it's not of length 4
        # if len(label) < self.max_length:
        #     label += [[0, 0, 0, 0, 0, 0]] * (self.max_length - len(label))
        return torch.tensor(image), torch.tensor(label)
        # return torch.from_numpy(image), torch.tensor(label)
#     def print_hello(self):
#         print('hello')
#         return label
