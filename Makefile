app-init:
	poetry run pre-commit autoupdate
	poetry run pre-commit install
