import random

def generate_unique_token(authorizations):
    token = generate_token()
    while any(s.token == token for s in authorizations):
        token = generate_token()
    return token

def generate_token():
    token = ''
    for x in range(20):
        token += chr(random.randrange(48,91))
    return token