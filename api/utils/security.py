import bcrypt


def hash_client_secret(plain_client_secret):
    if plain_client_secret is None or not isinstance(plain_client_secret, str):
        raise Exception()

    salt = bcrypt.gensalt()
    hashed_client_secret = bcrypt.hashpw(plain_client_secret.encode("utf-8"), salt)

    return hashed_client_secret.decode("utf-8")
