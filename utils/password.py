from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

def secure_pwd(raw_password: str) -> str:
    return pwd_context.hash(raw_password)

def verify_pwd(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)

# Handles password hashing and verification.

# Hashes raw passwords securely before storing in DB.

# Verifies a plain password against a hashed password when logging in.

# We switched to Argon2 because bcrypt was giving the 72-byte limit issue.