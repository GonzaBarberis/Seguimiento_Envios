FROM python:3.10
WORKDIR /botTrack
COPY requirements.txt /botTrack/
RUN pip install -r requirements.txt
COPY . /botTrack
ENV PATH "$PATH:/botTrack" 
CMD [ "python", "botTrack.py", "--host=0.0.0.0" ]
