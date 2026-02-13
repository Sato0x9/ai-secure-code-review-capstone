import tempfile

def create_temp():
    f = tempfile.mktemp()
    open(f, "w").write("data")
