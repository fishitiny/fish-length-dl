# Path: train.py

# The training script was written in Python and used PyTorch (Paszke et al., 2017) to train the regressor.
# The training data was split into 80% training and 20% validation data.
# The mean squared error was used as the loss function, and the Adam optimizer was used to minimize the loss.
# The learning rate was set to 0.001, and the batch size was set to 32.
# The model was trained for 125 epochs.
# The model was saved after training, and the loss and accuracy were recorded for each epoch.
# The training script was run on a single NVIDIA Tesla K80 GPU.
import torch
import torch.nn as nn
import torch.optim as optim

from model import FishRegressor
from dataset import FishDataset

# Set random seed for reproducibility
torch.manual_seed(0)

# Load the dataset
dataset = FishDataset()

# Split the dataset into training and validation sets
train_size = int(0.8 * len(dataset))
val_size = len(dataset) - train_size
train_dataset, val_dataset = torch.utils.data.random_split(dataset, [train_size, val_size])

# Create data loaders
train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=32, shuffle=True)
val_loader = torch.utils.data.DataLoader(val_dataset, batch_size=32, shuffle=False)

# Initialize the model
model = FishRegressor()

# Define the loss function and optimizer
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Train the model
for epoch in range(125):
    model.train()
    train_loss = 0.0
    for i, data in enumerate(train_loader, 0):
        inputs, labels = data
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
        train_loss += loss.item()
    train_loss /= len(train_loader)

    model.eval()
    val_loss = 0.0
    with torch.no_grad():
        for i, data in enumerate(val_loader, 0):
            inputs, labels = data
            outputs = model(inputs)
            loss = criterion(outputs, labels)
            val_loss += loss.item()
        val_loss /= len(val_loader)

    print(f'Epoch {epoch + 1}, Loss: {train_loss}')

# Save the model
torch.save(model.state_dict(), 'fish_regressor.pth')
