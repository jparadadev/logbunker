# Build project
.PHONY = build
build:
	python3 -m venv env
	pip3 install -r requirements.txt

# Install dependencies
.PHONY = deps
deps:
	pip3 install -r requirements.txt

# Run tests
.PHONY = test
test:
	python3 -m unittest discover -s ./tests -p '*Test.py'

# Run bunker
.PHONY = run/bunker
run/bunker:
	python3 -m logbunker --service bunker

# Run bunker
.PHONY = run/backoffice
run/backoffice:
	python3 -m logbunker --service backoffice

# Run all ctx
.PHONY = run/all
run/all:
	python3 -m logbunker --service all