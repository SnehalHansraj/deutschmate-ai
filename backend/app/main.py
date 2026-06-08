from fastapi import FastAPI

from app.api.auth import router as auth_router

app = FastAPI(
    title="DeutschMate API",
)

app.include_router(auth_router)

@app.get("/")
def root():
    return {
        "message": "DeutschMate API is running"
    }