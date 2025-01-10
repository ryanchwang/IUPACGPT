import numpy as np

def edge_to_ethane_name(edge_count):
    ethane_derivatives = {
        2: "ethane",
        3: "propane",
        4: "butane",
        5: "pentane",
        6: "hexane",
        7: "heptane",
        8: "octane",
        9: "nonane",
        10: "decane",    
    }

    return ethane_derivatives.get(edge_count, "unknown compound")