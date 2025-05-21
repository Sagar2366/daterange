"""Data models for date range overlap service."""

from datetime import datetime
from pydantic import BaseModel


class DateRange(BaseModel):
    """
    Represents a date range with start and end datetimes.
    """
    start: datetime
    end: datetime


class OverlapRequest(BaseModel):
    """
    Request model containing two date ranges to check for overlap.
    """
    range1: DateRange
    range2: DateRange


class OverlapResponse(BaseModel):
    """
    Response model indicating if ranges overlap and providing details.
    """
    overlap: bool
    details: str
