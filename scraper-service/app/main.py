from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def root():
    return {"msg": "Hello from scraper-service on port 8003!"}
