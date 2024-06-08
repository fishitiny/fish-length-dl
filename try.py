# 找到字符串中最后一个'.'的位置，然后将其后面的字符串删除
# def remove_suffix( s):
#     return s[:s.rfind('.')]
# #
# print(remove_suffix('3_05_21-B1.txt'))
# print(remove_suffix('3_05_21-B1.jpg'))
# print(remove_suffix('3_05_21-B1.txt') != remove_suffix('3_05_21-B1.jpg'))
# import dataset
# # # # import torch
# # # # # 判断dataset中label与data的数据类型
# dataset = dataset.FishDataset()
# x1, y1, x2, y2 = dataset.labels[0][0], dataset.labels[0][1], dataset.labels[0][2], dataset.labels[0][3]
# x1 = int(x1)
# y1 = int(y1)
# x2 = int(x2)
# y2 = int(y2)
#
# # # print(dataset.pos)
# import os
# # import numpy as np
import cv2
#
# # dataset = dataset.FishDataset()
# # label = dataset.labels[0]
# # image = dataset.data[0]
# # # 把data中的图片显示出来，注意把图片数据类型转换为numpy.ndarray
# # # list 类型转换为numpy.ndarray类型
# #
# # image = np.array(image)
# # image = image.transpose((1, 2, 0))
# # # print(image.shape)
# #
# #
# # x1, y1, x2, y2 = label[0], label[1], label[2], label[3]
# # x1 = int(x1)
# # y1 = int(y1)
# # x2 = int(x2)
# # y2 = int(y2)
# #
image = cv2.imread
cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
# cv2.rectangle(image, (10, 20), (75, 75), (0, 255, 0), 2)
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
#
#
# path = 'fish_tray_images_small'
# path_list = os.listdir(path)
# # path_list.remove('.DS_Store')
# path_list.sort(key=lambda x: int(x.split('_')[0]))
# path_label = 'fish_tray_labels'
#
#
# for file in os.listdir(path):
#     if file.split('.')[0] != dataset.name[0].split('.')[0]:
#         continue
#     # 打印名字
#     # [847.7244195210126, 376.70287271768996, 1005.6769546251346, 2266.348693193615]
#     x1=450
#     y1=100
#     x2=180
#     y2=600
#     print(file)
#     print(dataset.name[0])
#     image = cv2.imread(os.path.join(path, file))
#     image = cv2.resize(image, (1008, 756))
#     # 把除了x1,y1,x2,y2之外的部分填充为白色
#     print(x1, y1, x2, y2)
#     # 53.67063492063492,36.03670634920635,17.113095238095237,29.34027777777778
#     # if (x1 > x2):
#     #     t = x1
#     #     x1 = x2
#     #     x2 = t
#     # if (y1 > y2):
#     #     t = y1
#     #     y1 = y2
#     #     y2 = t
#
#     # 在x1,y1,x2,y2内画框
#     # image = image[y1:y2, x1:x2]
#     cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
# # 打印图片的尺寸
#     print(image.shape)
#     # image = cv2.resize(image, (200, 75))
#     cv2.imshow('Image', image)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
#     break
# # # 检查是否所有的labels的元素都能成功运行下面的代码
# # dataset.labels[0]+=[[0,0,0,0,0,0]] * (dataset.max_length - len(dataset.labels[0]))
# # # torch.tensor(dataset.labels[0])
# # # for image in dataset.data:
# # #     torch.tensor(image)
# # # torch.tensor(dataset.labels[1])
# #
# # print(dataset.labels[0])
#
# # dataset = dataset.FishDataset()
# # print(dataset.labels)
# # import os
# #
# # path = 'fish_tray_labels'
# # #计算txt文件中最多有多少行
# # i = 0
# # for file in os.listdir(path):
# #     with open(os.path.join(path, file)) as f:
# #         all_data = f.readlines()
# #         if len(all_data) > i:
# #             i = len(all_data)
# # print(i)
# # dictionary = {'Diplodus anularis': 0, 'Mullus barbatus': 1, 'Mullus surmulentus': '2','Pagellus acarne': 3,'Pagellus '
# #                                                                                                            'erythrinus': 4,'Pagrus pagrus': 5,'Scorpaena porcus': 6,'Sepia officinalis':7,'Serranus scriba': 8,'Sphyraena sphyraena': 9,'Spicara maena': 10,'Symphodus tinca H': 11,'Symphodus tinca M': 12}
# # path = 'fish_tray_labels'
# # path_list = os.listdir(path)
# # # path_list.remove('.DS_Store')
# # path_list.sort(key=lambda x: int(x.split('_')[0]))
# # # print(path_list)
# # for file in os.listdir(path):
# #     with open(os.path.join(path, file)) as f:
# #         for line in f:
# #             data = f.readline()
# #             data = data.split(',')
# #             # data = [float(x) for x in data]
# #             print(data)
#
#
# # import csv
# #
# # with open('size_estimation_homography_DeepFish.csv', 'r') as file:
# #     reader = csv.reader(file)
# #
# #     # 跳过第一行（假设它包含列字段）
# #     next(reader)
# #
# #     # 存储数据
# #     data = []
# #     for row in reader:
# #         data.append(row)
# #
# # # print(data[0][1])
# #
# # # =========================================
# # data = sorted(data, key=lambda x: int(x[1].split('_')[0]), reverse=False)  # 按第2个元素的值正序排列
# #
# # # 把data中的数据存储在labels中
# #
# # for row in data:
# #     result = row[2].rstrip("]")
# #     result = result.lstrip("[")
# #     result = result.split(", ")
# #     x1= float(result[0])/4032*200
# #     y1 = float(result[1])/3024*75
# #     x2 = float(result[2])/4032*200
# #     y2 = float(result[3])/3024*75
# #     result = [x1,y1,x2,y2]
# #     result.append(dictionary[row[3]])
# #     result.append(row[4])
# #     l = ""
# #     with open('fish_tray_labels/' + row[1] + '.txt', 'a') as fo:
# #         for z in result:
# #             l += "{}".format(z) + ","  # for下面一定要缩进，注意了
# #             print(l)
# #
# #         fo.write(l.strip(",")+ '\n')
#
#     # def safe(number):
#     #     try:
#     #         return int(number)
#     #     except:
#     #         try:
#     #             return float(number)
#     #         except:
#     #             return number
#
#
#     # result = list(map(safe, result))
#     # 将result存储在txt文件中，若不同row中row[1]元素相同，则将它们放在同一个文件中，文件名为row[1]+ '.txt'
#     # 若row[1]元素不同，则新建一个文件，文件名为row[1]+ '.txt'
#     # wj = open('fish_tray_labels/' + row[1] + '.txt', 'a')
#     #让result中的元素以逗号分隔，存储在txt文件中
#
#     # wj.write(str(result) + '\n')
# import os
# import numpy as np
# import cv2
#
#     # image = cv2.resize(image, (4032, 3024))
#     # image = image.transpose((2, 0, 1))
#     # image = image.astype(np.float32)
#     # image /= 255.0
#
# # # import os
# # #
# # # path = 'D:/.学习/智慧水产/项目/fish-length-prediction/fish_tray_images'
# # #
# # # path_list = os.listdir(path)
# # #
# # # # path_list.remove('.DS_Store')
# # #
# # # path_list.sort(key=lambda x: int(x.split('_')[0]))
# # #
# # # print(path_list)
# #
# # #=========================================
# #
# # import csv
# # #
# # # # 读取CSV文件
# # with open('size_estimation_homography_DeepFish.csv', 'r') as file:
# #     reader = csv.reader(file)
# #
# #     # 跳过第一行（假设它包含列字段）
# #     next(reader)
# #
# #     # 存储数据
# #     data = []
# #     for row in reader:
# #         data.append(row)
# #
# # # print(data[0][1])
# #
# # #=========================================
# # #已知两个二维列表
# # #第一个列表的元素是元组，按第 2 个元素的值从小到大排序输出，输出前 m 项
# # #第二个列表的元素是列表，按其每个元素第 1 个元素的值从小到大排序，输出前 n 项
# # #再按第二个列表每个元素第 3 个元素的值从小到大排序，输出前 n 项
# #
# # #list1.sort(key = lambda x:x[1],reverse = False) 和下面一行等价
# # data = sorted(data,key = lambda x:int(x[1].split('_')[0]),reverse = False)#按第2个元素的值正序排列
# #
# # for row in data:
# #     result = row[2].rstrip("]")
# #     result = result.lstrip("[")
# #     result = result.split(", ")
# #     result.append(row[3])
# #     result.append(row[4])
# #
# #
# #     def safe(number):
# #         try:
# #             return int(number)
# #         except:
# #             try:
# #                 return float(number)
# #             except:
# #                 return number
# #
# #
# #     result = list(map(safe, result))
# #     print(result)  # 输出："Hello, World!"
# #     # label.append()
# #     # print(label)
# #     print("\n")
# # # m = len(data)
# # # print(data[:m])
# # #
