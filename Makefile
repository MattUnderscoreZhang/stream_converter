.PHONY: twine twine_test

twine: build upload

build:
	pdm run python -m build

upload:
	pdm run twine upload --repository pypi dist/*
