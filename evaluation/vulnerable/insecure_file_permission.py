import os

with open("secret.txt", "w") as f:
    f.write("top secret")

os.chmod("secret.txt", 0o777)
