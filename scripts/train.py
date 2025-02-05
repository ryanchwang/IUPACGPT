import torch
import torch.optim as optim
import torch.nn as nn
from torch.utils.data import DataLoader
from model.hybrid_model import HybridModel
from model.dataset import MoleculeDataset
from config import *

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

dataset = MoleculeDataset(MONGO_URI, DB_NAME, COLLECTION_NAME)
dataloader = DataLoader(dataset, batch_size=BATCH_SIZE, shuffle=True)

model = HybridModel().to(device)
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=LEARNING_RATE)

for epoch in range(NUM_EPOCHS):
    for images, graphs, smiles in dataloader:
        images, graphs = images.to(device), graphs.to(device)

        optimizer.zero_grad()
        outputs = model(images, graphs)

        loss = criterion(outputs, smiles)
        loss.backward()
        optimizer.step()

    print(f"Epoch [{epoch+1}/{NUM_EPOCHS}], Loss: {loss.item():.4f}")

torch.save(model.state_dict(), "iupacgpt_model.pth")
