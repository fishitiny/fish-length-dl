# #写一段python代码，读取fish_tray_json_labels (1)文件夹中 1_06_21-B1__labels.json文件中species 32 类的所有label的regions里的坐标，并把它们画在fish_tray_images_2021_06-09文件夹中1_06_21-B1.jpg上
#
# import json
# import cv2
# import numpy as np
#
# # Load the JSON file
#
# with open('fish_tray_json_labels (1)/json/1_06_21-B1__labels.json') as f:
#     data = json.load(f)
# # Load the image
#
# image = cv2.imread('fish_tray_images_2021_06-09/1_06_21-B1.jpg')
#
# #region 中的坐标是一个list，里面有一个list，里面有若干个个字典，每个字典代表一个点的坐标
# # "regions": [
# #         [
# #           {
# #             "x": 1427,
# #             "y": 2027
# #           },
# #           {
# #             "x": 1427,
# #             "y": 2000
# #           },
# #           {
# #             "x": 1426,
# #             "y": 1994
# #           }
# #         ]
# #     ]
# # Loop over the regions
# for label in data['labels']:
#     #"object_id": "a99feac8-acf5-4028-bb51-1f5d70b7add3__6"
#     if label['label_class'] == 'sizeDmOjo':
#         # Loop through the regions
#         for region in label['regions']:
#             # Convert the coordinates to integers
#             coordinates = np.array([[point['x'], point['y']] for point in region]).astype(np.int32)
#             # Draw the polygon
#             cv2.polylines(image, [coordinates], isClosed=True, color=(0, 255, 0), thickness=2)
#
# # Display the image
# cv2.imshow('Image', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# #save the image in result/result.jpg
#
# cv2.imwrite('result/lengthHead.jpg', image)