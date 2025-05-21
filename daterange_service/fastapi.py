"""FastAPI app for checking overlap of date ranges."""

from fastapi import FastAPI
from daterange_service.models import OverlapRequest, OverlapResponse
from daterange_service.overlap import check_overlap

app = FastAPI()


@app.post("/overlap", response_model=OverlapResponse)
def overlap_endpoint(ranges: OverlapRequest):
    """
    Endpoint to check if two date ranges overlap.

    Args:
        ranges (OverlapRequest): The request body containing two date ranges.

    Returns:
        OverlapResponse: Result indicating whether the ranges overlap.
    """
    return check_overlap(ranges)
