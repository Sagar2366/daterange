"""Tests for the overlap API endpoint in daterange_service."""

from fastapi.testclient import TestClient
from daterange_service.app import app

client = TestClient(app)


def test_overlap_api_true():
    """
    Test that the /overlap endpoint returns overlap=True for overlapping ranges.
    """
    resp = client.post(
        "/overlap",
        json={
            "range1": {"start": "2025-05-20T12:00:00", "end": "2025-05-20T14:00:00"},
            "range2": {"start": "2025-05-20T13:00:00", "end": "2025-05-20T15:00:00"},
        },
    )
    assert resp.status_code == 200
    data = resp.json()
    assert data["overlap"] is True


def test_overlap_api_false():
    """
    Test that the /overlap endpoint returns overlap=False for non-overlapping ranges.
    """
    resp = client.post(
        "/overlap",
        json={
            "range1": {"start": "2025-05-20T12:00:00", "end": "2025-05-20T13:00:00"},
            "range2": {"start": "2025-05-20T13:00:00", "end": "2025-05-20T14:00:00"},
        },
    )
    assert resp.status_code == 200
    data = resp.json()
    assert data["overlap"] is False
