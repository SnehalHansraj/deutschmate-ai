from app.core.jwt import create_access_token
from jose import jwt

token = create_access_token(
    {
        "sub": "1"
    }
)

print(token)

decoded = jwt.get_unverified_claims(token)

print(decoded)