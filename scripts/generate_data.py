from rdkit import Chem
from rdkit.Chem import Draw
import os

def generate_images(smiles_list, output_dir="data/"):
    os.makedirs(output_dir, exist_ok=True)
    for i, smiles in enumerate(smiles_list):
        mol = Chem.MolFromSmiles(smiles)
        img = Draw.MolToImage(mol)
        img.save(f"{output_dir}/molecule_{i}.png")

smiles_data = ["CC", "CCC", "CCCC", "COO"]  # Replace with more SMILES
generate_images(smiles_data)
