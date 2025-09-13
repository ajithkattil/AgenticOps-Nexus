.PHONY: run-users db-init lint test

run-users:
	uvicorn services.users.app.main:app --reload --port 8001

db-init:
	python services/users/app/db.py --init

lint:
	ruff check .

test:
	pytest -q
