FROM jfloff/alpine-python
WORKDIR /usr/src/app
COPY ./code /usr/src/app
RUN pip install -r requirements.txt
CMD [ "python", "main.py" ]