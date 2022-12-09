FROM python:3

WORKDIR /aoc

COPY requirements.txt .
RUN pip install -r requirements.txt

ENV PYTHONPATH=/aoc

COPY . .

CMD ["python", "main.py"]
