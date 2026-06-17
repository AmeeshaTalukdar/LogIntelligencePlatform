from fastapi import FastAPI
from pydantic import BaseModel
from service import classify_log

app = FastAPI(title="Log Intelligence API")

class LogRequest(BaseModel):
    source: str
    log: str

@app.post("/classify")
def classify(req: LogRequest):
    return classify_log(req.source, req.log)