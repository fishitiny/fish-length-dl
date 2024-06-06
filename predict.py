# Path: predict.py

# The prediction script was written in Python and used PyTorch (Paszke et al., 2017) to load the trained model and make predictions on new data.
# The script loaded the trained model and a new image of a fish.
# The image was preprocessed to match the input format of the model.

# The model was used to predict the length and coordinates of the fish in the image.
# The predictions were printed to the console.
# The prediction script was run on a single NVIDIA Tesla K80 GPU.

import torch
import cv2
import numpy as np

from model import FishRegressor

# Load the trained model
model = FishRegressor()
model.load_state_dict(torch.load('fish_regressor.pth'))
model.eval()

# Load the image
image = cv2.imread('12_04_21-B.9.jpg')
image = cv2.resize(image, (200, 75))
image = image.transpose((2, 0, 1))
image = np.expand_dims(image, axis=0)
image = image.astype(np.float32)
image /= 255.0

# Convert the image to a PyTorch tensor
image = torch.from_numpy(image)

# Make a prediction
with torch.no_grad():
    prediction = model(image)
    prediction = prediction.numpy()

print(f'Predicted Specie: {prediction[0][0]}')
print(f'Predicted Length: {prediction[0][1]}')

# image = cv2.imread('3_05_21-B23.jpg')
# image = cv2.resize(image, (200, 75))
# x1 = int(prediction[0][0])
# y1 = int(prediction[0][1])
# x2 = int(prediction[0][2])
# y2 = int(prediction[0][3])
# cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

# cv2.imshow('Image', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#print(f'Predicted Length: {prediction[0][4]}')
