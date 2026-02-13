import pickle

def load_data(filename):
    with open(filename, "rb") as f:
        return pickle.load(f)
