from fastapi import FastAPI
from daterange_service.models import OverlapRequest, OverlapResponse
from daterange_service.overlap import check_overlap

app = FastAPI()

@app.post("/overlap", response_model=OverlapResponse)
def overlap_endpoint(ranges: OverlapRequest):
    return check_overlap(ranges)
