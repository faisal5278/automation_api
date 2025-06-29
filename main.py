from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from database import insert_test_result, get_all_results, update_test_status, get_summary

app = FastAPI()

# Pydantic model for input validation
class TestResult(BaseModel):
    module_name: str
    status: str
    timestamp: Optional[str] = None

class StatusUpdate(BaseModel):
    status: str

@app.get("/health")
def health_check():
    return {"status": "API is running!"}

@app.post("/log_test_result")
def log_test_result(result: TestResult):
    if result.status not in ["pass", "fail"]:
        raise HTTPException(status_code=400, detail="Status must be 'pass' or 'fail'")
    new_id = insert_test_result(result.module_name, result.status, result.timestamp)
    return {"message": "Test result logged", "id": new_id}

@app.get("/get_all_results")
def get_results():
    results = get_all_results()
    return {"results": results}

@app.get("/get_summary")
def get_test_summary():
    total, passed, failed = get_summary()
    return {
        "total": total,
        "passed": passed,
        "failed": failed
    }

@app.put("/update_test_status/{test_id}")
def update_status(test_id: int, update: StatusUpdate):
    if update.status not in ["pass", "fail"]:
        raise HTTPException(status_code=400, detail="Status must be 'pass' or 'fail'")
    updated_rows = update_test_status(test_id, update.status)
    if updated_rows == 0:
        raise HTTPException(status_code=404, detail="Test result not found")
    return {"message": "Status updated"}
