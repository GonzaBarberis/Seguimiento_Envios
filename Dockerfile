FROM python:3.10
WORKDIR /botTrack
COPY requirements.txt /botTrack/
RUN pip install -r requirements.txt
RUN wget https://chromedriver.storage.googleapis.com/106.0.5249.61/chromedriver_linux64.zip
RUN unzip chromedriver_linux64.zip
RUN chmod a+xrw chromedriver
COPY . /botTrack
ENTRYPOINT ["python3"]
#ENV PATH "$PATH:/" 
CMD [ "botTrack.py"]
