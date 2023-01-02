FROM python:3.10
WORKDIR /botTrack
COPY requirements.txt /botTrack/
RUN pip install -r requirements.txt
COPY . /botTrack
CMD python botTrack.py
ENV PATH=C:\Users\usuario\Desktop\Bots\BotTrackPY\chromedriver.exe
