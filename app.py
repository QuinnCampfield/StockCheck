# app.py
from fastapi import FastAPI, Query
from pipeline import run_ingest, get_data
from llm_utils import answer_question

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Financial Data Assistant API", "status": "healthy"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/ingest")
def ingest(tickers: list[str] = Query(None, description="List of tickers to ingest (optional)")):
    run_ingest(tickers)
    return {"status": "ingested"}

@app.get("/ask")
def ask(q: str = Query(..., description="Your financial question")):
    data = get_data()
    response = answer_question(q, data)
    print(response)
    return {"answer": response}
