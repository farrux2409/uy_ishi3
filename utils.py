import bcrypt


def hash_password(raw_password):
    encoded_password = raw_password.encode('utf-8')
    salt = bcrypt.gensalt(4)
    hashed_password = bcrypt.hashpw(encoded_password, salt)
    return hashed_password


def check_password(user_password, hashed_password):
    encoded_password1 = user_password.encode('utf-8')
    return bcrypt.checkpw(encoded_password1, hashed_password)


print(check_password('123', hash_password(raw_password='123')))
