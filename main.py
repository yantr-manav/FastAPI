from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def greet():
    return f"message: Welcome to the world of Python!"

