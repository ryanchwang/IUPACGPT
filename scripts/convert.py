from rdkit.Chem import MolToSmiles, MolToInchiKey

def smiles_to_iupac(smiles):
    mol = Chem.MolFromSmiles(smiles)
    return Chem.MolToSmiles(mol)
