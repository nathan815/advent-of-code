file ?= main.py

build:
	docker build -t advent-of-code-2022 .

run:
	docker run -it -v $(shell pwd):/aoc advent-of-code-2022 python $(file)

test:
	docker run -it -v $(shell pwd):/aoc advent-of-code-2022 pytest

bash:
	docker run -it -v $(shell pwd):/aoc advent-of-code-2022 bash