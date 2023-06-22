import bcrypt


def generate_password(password):
    return bcrypt.hashpw(password=password.encode(), salt=bcrypt.gensalt()).decode()


def validate_password(password, hashed_password):
    ok = bcrypt.checkpw(password=password.encode(), hashed_password=hashed_password.encode())
    return ok


if __name__ == "__main__":
    pwd = "123"
    h_pwd = generate_password(pwd)
    print(h_pwd)
    ok = validate_password("mima", h_pwd)
    print(ok)
    ok = validate_password("mimaa", h_pwd)
    print(ok)
