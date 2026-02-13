def read_file(filename):
    with open("files/" + filename, "r") as f:
        return f.read()
