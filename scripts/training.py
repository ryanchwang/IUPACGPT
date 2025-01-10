import torch
from torch.utils.data import DataLoader, Dataset
from model import MoleculeCNN

class MoleculeDataset(Dataset):
    def __init__(self, images, labels):
        self.images = images
        self.labels = labels

    def __len__(self):
        return len(self.images)

    def __getitem__(self, idx):
        return self.images[idx], self.labels[idx]

def train_model(model, dataloader, optimizer, loss_fn, epochs=5):
    for epoch in range(epochs):
        for images, labels in dataloader:
            images, labels = images.to(device), labels.to(device)
            optimizer.zero_grad()
            outputs = model(images)
            loss = loss_fn(outputs, labels)
            loss.backward()
            optimizer.step()
        print(f"Epoch {epoch + 1}, Loss: {loss.item()}")

# Example setup
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = MoleculeCNN().to(device)
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
loss_fn = torch.nn.CrossEntropyLoss()

# Replace with actual DataLoader
train_loader = DataLoader(MoleculeDataset(...), batch_size=32, shuffle=True)
train_model(model, train_loader, optimizer, loss_fn)
