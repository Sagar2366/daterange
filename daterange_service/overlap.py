"""Logic for checking overlap between two date ranges."""

from daterange_service.models import OverlapRequest, OverlapResponse


def check_overlap(ranges: OverlapRequest) -> OverlapResponse:
    """
    Check whether two date ranges overlap and provide details.

    Args:
        ranges (OverlapRequest): The request containing two date ranges.

    Returns:
        OverlapResponse: Response indicating if there is overlap and the details.
    """
    r1 = ranges.range1
    r2 = ranges.range2

    latest_start = max(r1.start, r2.start)
    earliest_end = min(r1.end, r2.end)

    if latest_start < earliest_end:
        return OverlapResponse(
            overlap=True,
            details=(
                f"Ranges overlap between "
                f"{latest_start.isoformat()} and {earliest_end.isoformat()}"
            )
        )
    else:
        return OverlapResponse(
            overlap=False,
            details="No overlap"
        )
