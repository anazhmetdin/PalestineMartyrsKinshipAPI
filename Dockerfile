FROM python:3.8 
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
COPY requirements.txt /
RUN pip install -r /requirements.txt
RUN git clone https://github.com/MTG/ArabicTransliterator.git
WORKDIR /ArabicTransliterator
RUN python setup.py install
RUN pip install -e .
WORKDIR /
RUN mkdir /code
WORKDIR /code 
COPY . /code/