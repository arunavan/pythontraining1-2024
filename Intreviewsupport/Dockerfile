FROM python:3.12

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
#RUN pip install flask
COPY . .

CMD [ "python", "-m" , "flask", "run", "--host=localhost"]