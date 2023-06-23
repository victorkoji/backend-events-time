FROM python:3.9-slim-buster

WORKDIR /app

RUN mkdir src
RUN mkdir config

COPY . . 

RUN pip3 install -r requirements.txt

ENV FLASK_APP=src/app.py

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--debug"]
