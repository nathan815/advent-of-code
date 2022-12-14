# Advent of Code

https://adventofcode.com/


## Set up

**Prereq:** Docker

```
cd 2022
make build
# or: docker build -t advent-of-code-2022 .
```

## Run

### Run all solutions

`make run`

or `docker run -it advent-of-code-2022`

### Run specific solution

`make run file=day5/part1.py`

or `docker run -it advent-of-code-2022 python day5/part1.py`

### Run unit tests
`make test`

or `docker run -it advent-of-code-2022 pytest`
