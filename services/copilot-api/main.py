from fastapi import FastAPI
from pydantic import BaseModel
import duckdb

app = FastAPI()
con = duckdb.connect("/data/factory.db", read_only=False)

class KPIQuery(BaseModel):
    prompt: str

@app.post("/kpi")
async def kpi(q: KPIQuery):
    # TODO: LangChain → SQL 변환
    return {"rows": [], "sql": "-- coming soon"}
