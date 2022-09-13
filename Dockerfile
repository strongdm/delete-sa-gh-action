FROM continuumio/miniconda3

RUN apt update -y
RUN apt install -y git

COPY *.py /
COPY requirements.txt /

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "/main.py"]
