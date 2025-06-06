"""Unit tests for the check_overlap function in daterange_service."""

from datetime import datetime
from daterange_service.models import DateRange, OverlapRequest
from daterange_service.overlap import check_overlap


def dt(s):
    """
    Convert ISO format string to datetime object.

    Args:
        s (str): ISO format datetime string.

    Returns:
        datetime: Corresponding datetime object.
    """
    return datetime.fromisoformat(s)


def test_overlap_true():
    """
    Test that check_overlap returns overlap=True for overlapping ranges.
    """
    req = OverlapRequest(
        range1=DateRange(start=dt("2025-05-20T12:00:00"), end=dt("2025-05-20T14:00:00")),
        range2=DateRange(start=dt("2025-05-20T13:00:00"), end=dt("2025-05-20T15:00:00")),
    )
    resp = check_overlap(req)
    assert resp.overlap is True
    assert "overlap" in resp.details


def test_overlap_false():
    """
    Test that check_overlap returns overlap=False for non-overlapping ranges.
    """
    req = OverlapRequest(
        range1=DateRange(start=dt("2025-05-20T12:00:00"), end=dt("2025-05-20T13:00:00")),
        range2=DateRange(start=dt("2025-05-20T13:00:00"), end=dt("2025-05-20T14:00:00")),
    )
    resp = check_overlap(req)
    assert resp.overlap is False
    assert resp.details == "No overlap"
