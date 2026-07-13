from fastapi import FastAPI

app = FastAPI(
    title="Post Service",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "Post Service is Running 🚀"
    }