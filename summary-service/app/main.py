from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def root():
    return {"msg": "Hello from summary-service on port 8004!"}
