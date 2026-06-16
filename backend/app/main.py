from fastapi import FastAPI

from app.api.auth import (
    router as auth_router
)

from app.api.progress import (
    router as progress_router
)

app = FastAPI(
    title="DeutschMate API",
)

app.include_router(auth_router)
app.include_router(progress_router)


@app.get("/")
def root():
    return {
        "message": "DeutschMate API is running"
    }