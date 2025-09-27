from pydantic import BaseModel
from typing import List, Optional

class SlotAssignment(BaseModel):
    course_code: str
    batch_id: str
    faculty_id: str
    room_id: str
    day: str
    slot: str

class GenerateRequest(BaseModel):
    # Define fields matching your input JSON schema
    # Example:
    faculties: List[dict]
    rooms: List[dict]
    courses: List[dict]
    batches: List[dict]
    constraints: Optional[List[dict]] = []

class TimetableResponse(BaseModel):
    assignments: List[SlotAssignment]
    success: bool
    message: Optional[str] = None
