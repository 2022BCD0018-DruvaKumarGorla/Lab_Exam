from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API Running-BCD018"}

@app.post("/predict")
def predict(data: dict):
    if "input" not in data:
        return {"error": "Invalid Input - BCD0018"}
    return {"result": f"Processed: {data['input']}"}