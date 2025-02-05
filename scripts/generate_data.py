from rdkit import Chem
from rdkit.Chem import Draw
import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import io
from pymongo import gridfs
import requests
import pymongo
from rdkit import Chem
from rdkit.Chem import Draw
from io import BytesIO


uri = "mongodb+srv://ryanchwang:5dFaLqK2iEprwvVk@iupac.y5dij.mongodb.net/?retryWrites=true&w=majority&appName=IUPAC"
# Create a new client and connect to the server
client = MongoClient(uri)
db = client["moleculeDataset"]

def fetch_smiles_from_chembl(num_molecules):
    """
    Fetch random SMILES from ChEMBL database using their API.
    """
    url = f"https://www.ebi.ac.uk/chembl/api/data/molecule.json?limit={num_molecules}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        smiles_list = [mol["molecule_structures"]["canonical_smiles"] for mol in data["molecules"] if mol["molecule_structures"]]
        return smiles_list
    else:
        print("Error fetching data from ChEMBL API.")
        return []

def extract_graph_features(mol):
    """
    Extracts graph-based features (nodes, edges) for GNN.
    """
    nodes = [atom.GetAtomicNum() for atom in mol.GetAtoms()]  # Atomic numbers as node features
    edges = []
    edge_types = []

    for bond in mol.GetBonds():
        start = bond.GetBeginAtomIdx()
        end = bond.GetEndAtomIdx()
        bond_type = bond.GetBondTypeAsDouble()  # Converts to single(1.0), double(2.0), etc.

        edges.append((start, end))
        edges.append((end, start))  # Since undirected graph
        edge_types.append(bond_type)
        edge_types.append(bond_type)

    return {"nodes": nodes, "edges": edges, "edge_types": edge_types}

def generate_and_store(num_molecules=10, db_name="iupacgpt", collection_name="molecules"):
    """
    Generate molecular images, extract graph features, and store them in MongoDB.
    """
    # Connect to MongoDB Atlas
    client = pymongo.MongoClient(MONGO_URI)
    db = client[db_name]
    collection = db[collection_name]

    # Fetch SMILES from ChEMBL
    smiles_list = fetch_smiles_from_chembl(num_molecules)

    for smiles in smiles_list:
        mol = Chem.MolFromSmiles(smiles)
        if mol is None:
            continue  # Skip invalid molecules

        # Generate molecule image
        img = Draw.MolToImage(mol)

        # Convert image to binary
        img_byte_arr = BytesIO()
        img.save(img_byte_arr, format="PNG")
        img_data = img_byte_arr.getvalue()

        # Extract graph-based features for GNN
        graph_data = extract_graph_features(mol)

        # Store in MongoDB
        molecule_data = {
            "smiles": smiles,
            "iupac_name": Chem.MolToInchi(mol),  
            "image": img_data,  
            "graph": graph_data  # Store graph structure
        }
        collection.insert_one(molecule_data)

    print(f"✅ Successfully stored {num_molecules} molecules in MongoDB!")

# Run the generator with desired number of molecules
if __name__ == "__main__":
    generate_and_store(num_molecules=50)  # Change this number as needed
