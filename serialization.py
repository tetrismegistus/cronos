import pickle


def save_file(filename, data):
    with open(filename, 'wb') as f:
        pickle.dump(data, f)


def load_file(filename):
    with open(filename, 'rb') as f:
        data = pickle.load(f)
    return data
