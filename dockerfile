FROM jfloff/alpine-python
WORKDIR /usr/src/pingbot
COPY ./code .
RUN pip install -r requirements.txt
CMD [ "python", "main.py" ]