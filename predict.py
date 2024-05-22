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
image = cv2.imread('fish.jpg')
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

print(f'Predicted Coordinates: ({prediction[0][0]}, {prediction[0][1]}), ({prediction[0][2]}, {prediction[0][3]})')

print(f'Predicted Specie: {prediction[0][4]}')
print(f'Predicted Length: {prediction[0][5]}')

#print(f'Predicted Length: {prediction[0][4]}')
