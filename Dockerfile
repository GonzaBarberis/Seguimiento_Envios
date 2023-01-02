FROM python:3.10
WORKDIR /botTrack
ADD botTrack.py /
COPY requirements.txt /botTrack/
RUN pip install -r requirements.txt
COPY . /botTrack
CMD [ "python", "./botTrack.py" ]
