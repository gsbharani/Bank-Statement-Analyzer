from passlib.context import CryptContext
import jwt
import os

pwd_context = CryptContext(schemes=["bcrypt"])

SECRET = os.getenv("SECRET_KEY")

def hash_password(password):
    return pwd_context.hash(password)

def verify_password(password, hashed):
    return pwd_context.verify(password, hashed)

def create_token(email):
    return jwt.encode({"sub": email}, SECRET, algorithm="HS256")
