from fastapi import FastAPI

app = FastAPI(
    title="DeutschMate API",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "DeutschMate API is running"
    }