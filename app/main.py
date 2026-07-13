from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Welcome to my API"}


@app.get("/about")
def about():
    return {
        "name": "Pranjal",
        "course": "B.Tech CSE AI & ML"
    }


@app.get("/contact")
def contact():
    return {
        "email": "pranjal@example.com"
    }


@app.get("/college")
def college():
    return {
        "college": "UPES",
        "city": "Dehradun"
    }