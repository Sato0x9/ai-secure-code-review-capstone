def save_user(username, password):
    with open("users.txt", "a") as f:
        f.write(f"{username}:{password}\n")
