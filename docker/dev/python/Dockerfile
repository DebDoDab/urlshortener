FROM python:3.8.3
MAINTAINER deb1337@gmail.com

WORKDIR /usr/shr/app

COPY requirements.txt ./
RUN pip3 install -r requirements.txt

COPY ./app ./app

CMD ["uvicorn", "app.main.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]