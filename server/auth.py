from passlib.context import CryptContext

# Configure bcrypt for password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# Hash the password before storing it
def hash_password(password: str):
    return pwd_context.hash(password)


# Verify the entered password with the stored hash
def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)