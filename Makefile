install:
	pip install -r requirements.txt

clean:
	rm -f .coverage*
	rm -rf __pycache__
	rm -rf bb84/__pycache__
	rm -rf tests/__pycache__

lint:
	pylint bb84 bb84/tests bb84/cascade bb84/cascade/tests

test:
	rm -f .coverage*
	pytest -v --cov --cov-report=html bb84/cascade/tests
	pytest -v --cov --cov-report=html bb84/tests

test-detailed:
	rm -f .coverage*
	pytest -v -s --cov --cov-report=html bb84/cascade/tests
	pytest -v -s --cov --cov-report=html bb84/tests

pre-commit: lint test
	@echo "OK"

.PHONY: install clean lint test test-detailed pre-commit