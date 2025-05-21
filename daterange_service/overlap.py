from daterange_service.models import OverlapRequest, OverlapResponse

def check_overlap(ranges: OverlapRequest) -> OverlapResponse:
    r1 = ranges.range1
    r2 = ranges.range2

    latest_start = max(r1.start, r2.start)
    earliest_end = min(r1.end, r2.end)

    if latest_start < earliest_end:
        return OverlapResponse(
            overlap=True,
            details=f"Ranges overlap between {latest_start.isoformat()} and {earliest_end.isoformat()}"
        )
    else:
        return OverlapResponse(
            overlap=False,
            details="No overlap"
        )
