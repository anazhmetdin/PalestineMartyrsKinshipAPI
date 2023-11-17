FROM python:3.8 
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
COPY requirements.txt /
COPY wheels/ /wheels/
RUN pip install -r /requirements.txt
RUN mkdir /code
WORKDIR /code 
COPY . /code/
EXPOSE 8080