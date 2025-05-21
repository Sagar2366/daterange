.PHONY: build test run artifact clean

build:
	pip install -r requirements.txt

test:
	PYTHONPATH=. pytest

run:
	uvicorn daterange_service.fastapi:app --reload

artifact:
	tar czvf daterange_service.tar.gz daterange_service/*.py requirements.txt

clean:
	rm -f daterange_service.tar.gz
