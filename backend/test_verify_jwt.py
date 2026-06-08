from app.core.jwt import (
    create_access_token,
    verify_access_token
)

token = create_access_token(
    {
        "sub": "1"
    }
)

print("TOKEN:")
print(token)

print("\nPAYLOAD:")

payload = verify_access_token(token)

print(payload)