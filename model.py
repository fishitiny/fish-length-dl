import torch
import torch.nn as nn
import torch.nn.functional as F

class FishRegressor(nn.Module):

    def __init__(self):
        super(FishRegressor, self).__init__()
        #The filter size for the convolutional layers was set to 3x3, and the stride was set to 1.
        #The number of filters was set to 32 for the first convolutional layer and 64 for the second and third convolutional layers.
        #for conv1, input channel means the number of channels of the input image. The reason is that the input image is a color image, which has three channels: red, green, and blue.
        self.conv1 = nn.Conv2d(3, 32, 3)

        self.conv2 = nn.Conv2d(32, 64, 3)
        self.conv3 = nn.Conv2d(64, 64, 3)
        #self.fc1 = nn.Linear(64 * 5 * 16, 256)
        # self.fc2 = nn.Linear(256, 5)
        self.fc1 = nn.Linear(64 * 5 * 16, 256)
        self.fc2 = nn.Linear(256, 6)
    def forward(self, x):
        x = F.max_pool2d(F.relu(self.conv1(x)), (2, 2))
        x = F.max_pool2d(F.relu(self.conv2(x)), (2, 2))
        x = F.max_pool2d(F.relu(self.conv3(x)), (2, 2))

        #x.view means to reshape the tensor x to the desired shape. The -1 means that the size of that dimension is inferred from the other dimensions.
        x = x.view(-1, self.num_flat_features(x))
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return x

    def num_flat_features(self, x):
        size = x.size()[1:]
        num_features = 1
        for s in size:
            num_features *= s
        return num_features
