# Build project dependencies
deps-install:
	source .venv/bin/activate && pip install -r requirements.txt

make-deps:
	pip freeze > requirements.txt

deps-upgrade:
	pip freeze --local | \
	grep -v '^\-e' | \
	cut -d = -f 1  | \
	xargs -n1 pip install -U

build: deps-install
	echo 'placeholder build task!'
	
run:
	python main.py