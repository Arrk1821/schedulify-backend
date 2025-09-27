from fastapi import FastAPI
from schemas import GenerateRequest, TimetableResponse
from scheduling import generate_timetable

app = FastAPI()

@app.get("/")
def home():
    return {"message": "FastAPI scheduling service is running"}

@app.post("/generate", response_model=TimetableResponse)
def generate(req: GenerateRequest):
    assignments = generate_timetable(req)
    return TimetableResponse(assignments=assignments, success=True)
