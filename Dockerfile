#### View all to know what to comment and uncomment
####--------------------------------
###
## Install Python
####

FROM python:3.7-stretch

####
##  Create app directory
### 

WORKDIR /usr/src/app

####
## Copy project to WORKDIR
####
COPY . ./

####
## Install app dependencies
####

RUN pip install -r requirements.txt

EXPOSE 5000
####
## Run python script
####

ENTRYPOINT ["python"]

CMD [ "run.py"]

####--------------------------------


