# DateRange Overlap API

A small, JSON-based API service to determine if two date ranges overlap.

## Usage

Start the service:
```
make build
make run
```

POST to `/overlap` with:
```json
{
  "range1": {"start": "2025-05-20T12:00:00Z", "end": "2025-05-20T14:00:00Z"},
  "range2": {"start": "2025-05-20T13:30:00Z", "end": "2025-05-20T15:00:00Z"}
}
```

Response:
```json
{
  "overlap": true,
  "details": "Ranges overlap between 2025-05-20T13:30:00+00:00 and 2025-05-20T14:00:00+00:00"
}
```

## Build/Test/Artifact
- `make build` - Install dependencies
- `make test` - Run tests
- `make artifact` - Build a tar.gz of the service

## Requirements
- Python 3.8+
- FastAPI
