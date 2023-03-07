FROM ubuntu:18.04
MAINTAINER velsrumao@gmail.com

#TO GET THE BASE PACKAGES INSTALLED ON THE INSTANCE
RUN apt-get update -y
RUN apt-get install python3-pip -y
RUN apt-get install gunicorn3 -y

#COPY APP FOLDER AND ITS DEPENDENCIES ON THE INSTANCE 
COPY requirements.txt requirements.txt
COPY flaskapp /opt/

#INSTALL THE PACKAGES ON THE DOCKER 
RUN pip3 install -r requirements.txt
WORKDIR /opt/

CMD ["gunicorn3", "-b", "0.0.0.0:8000", "app:app", "--workers=5"]
