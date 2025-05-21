from pydantic import BaseModel
from datetime import datetime

class DateRange(BaseModel):
    start: datetime
    end: datetime

class OverlapRequest(BaseModel):
    range1: DateRange
    range2: DateRange

class OverlapResponse(BaseModel):
    overlap: bool
    details: str
