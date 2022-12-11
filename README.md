# Predicting Short-Term Traffic Flow Congestion On Urban Motorway Networks

## DESCRIPTION 
<p align="center"> 
 <img width="200" height="200" src="https://github.com/taiwotman/TensorflowPredictCongestionTypes/blob/master/miscellanous/smart-traffic.png"></p>
 <p align="center">
<img width="200" height="200" src="https://github.com/taiwotman/TensorflowPredictCongestionTypes/blob/master/miscellanous/high-congestion.png">
 <img width="200" height="200" src="https://github.com/taiwotman/TensorflowPredictCongestionTypes/blob/master/miscellanous/medium-congestion.png">
 <img width="200" height="200" src="https://github.com/taiwotman/TensorflowPredictCongestionTypes/blob/master/miscellanous/low-congestion.png">
</p>

<p align="justify">
A system and method for the prediction of vehicle traffic congestion on a given roadway within a region. In particular, the computer implemented method of the present disclosure utilize real time traffic images from traffic cameras for the input of data and utilizes computer processing and machine learning to model a predictive level of congestion within a category of low congestion, medium congestion, or high congestion. By implementing machine learning in the comparison of exemplary images and administrator review, the computer processing system and method steps can predict a more efficient real-time congestion over time.
</p>

* Read the [WhitePaper](https://github.com/taiwotman/Smart-Traffic/blob/master/miscellanous/Whitepaper.pdf)
* View the [Slide Deck](https://docs.google.com/presentation/d/1ecyTVmE2eLL8S8tCIGs8JBKw0EEAsHAqw2U0Yq0A_Ns/edit?usp=sharing)

### Dependencies
![Python](https://img.shields.io/badge/Python-v3.7-blue.svg?logo=python&longCache=true&logoColor=white&colorB=5e81ac&style=flat-square&colorA=4c566a)
![Tensorflow](https://img.shields.io/badge/Tensorflow-v2.8.0-blue.svg?longCache=true&logo=python&style=flat-square&logoColor=white&colorB=5e81ac&colorA=4c566a)
![Flask](https://img.shields.io/badge/Flask-v2.0.2-blue.svg?longCache=true&logo=flask&style=flat-square&logoColor=white&colorB=5e81ac&colorA=4c566a)
![Urllib3](https://img.shields.io/badge/Urllib3-v1.24.3-blue.svg?longCache=true&logo=python&style=flat-square&logoColor=white&colorB=5e81ac&colorA=4c566a)
![Numpy](https://img.shields.io/badge/Numpy-v1.13.3-blue.svg?longCache=true&logo=python&style=flat-square&logoColor=white&colorB=5e81ac&colorA=4c566a)
![WTForms](https://img.shields.io/badge/WTForms-v2.1-blue.svg?longCache=true&logo=python&style=flat-square&logoColor=white&colorB=5e81ac&colorA=4c566a)
![Werkzeug](https://img.shields.io/badge/Werkzeug-v0.7-blue.svg?longCache=true&logo=python&style=flat-square&logoColor=white&colorB=5e81ac&colorA=4c566a)



### REPOSITORY

**RELEASE VERSION  1.1.0**

- Create Flask REST API using (real-time) traffic image  data for prediction.

- Implement search query based on region
      
- Make Jinja template to display parameters on index.page 

- On Index page, display traffic images with URL and add dropdown selections with regions

- Clean template
      
- Add Prediction features


## SET UP
### LOCAL ENVIRONMENT

**1. Clone git repository and `cd` into the directory**

     git clone https://github.com/taiwotman/Smart-Traffic.git

**2. Set up [virtualenv](https://virtualenv.pypa.io/en/stable/) with directory _venv_** 

     virtualenv venv

**3. Activate _venv_ using:**

     source venv/bin/activate

**4. Pip install requirements:**

     pip install -r requirements.txt
 
**5. Run command**
     
     python run.py

__Sample Test Case__

<p align="center">
 <img width="500" height="500" src="https://github.com/taiwotman/Smart-Traffic/blob/master/miscellanous/Architecture%20of%20real-time%20prediction.png">
</p>

**6. To implement the following test, use the [development branch](https://github.com/taiwotman/Smart-Traffic/tree/development).**

**7. Run the following python command with the  traffic congestion image(supports only jpeg/jpg format) as argument. For example:**

     python run.py test_image/Aut10_010.jpg
     
**8. Sample output:**

     high congestion (score = 0.70454)



### AUTHORIZATION HEADER

***In json_parser***

    headers= {
                    "Authorization": "************",
                    "Connection": "keep-alive" 
              }
      
### DOCKER

    docker build -t taiwotman/smart-traffic:latest .

    docker run --rm -p 80:5000 taiwotman/smart-traffic:latest 

Open on [browser](https://localhost:80)

### AWS EKS

    kubectl apply -f aws_eks/deployment.yaml 

smart-traffic-service  deployment.apps/smart-traffic created

http://localhost:8080/api/v1/namespaces/default/services/smart-traffic-service/proxy

Delete cluster

    eksctl delete cluster --region=us-east-2 --name=smart-cluster


### GCP

     gcloud app deploy

**PS:** _deploy might take few minutes_

### Likely issues

1. if error on starting, reinitialize project using:

     gcloud app init

2. ERROR: (gcloud.app.deploy) INVALID_ARGUMENT: unable to resolve source

   Go to storage bucket and delete app storage. Then redeploy app.
   
3. Latency -  Takes an average of 1 min to return predictions on the local environment.

4. No results return- Obtain authorization key

### ACKNOWLEDGEMENTS

So much gratitude to [New South Wales Transport Agency](www.transport.nsw.gov.au) for the open live traffic data API
and Google for the [Tensorflow](https://www.tensorflow.org/). 
Without opensource contributions this work would not have been derived.


### WANT TO BE CONTRIBUTOR?

1. Fork repository

     and/or

2. Send a [message](https://taiwotman.github.io/#contact).

**FOR ACADEMIC PURPOSE; kindly, cite our related work:**

 T. Adetiloye, A. Awasthi  (2019). Multimodal Big Data Fusion for Traffic Congestion Prediction. 
     In: Seng K., Ang L., Liew   AC., Gao J. (eds) Multimodal Analytics for Next-Generation Big Data Technologies 
     and Applications(pg. 319-335). doi: https://doi.org/10.1007/978-3-319-97598-6_13. Springer, Cham.
 
 T. Adetiloye, A. Awasthi  (2018).  Traffic Condition Monitoring Using Social Media Analytics. 
     In: Roy, S., Samui, P., Deo, R., Ntalampiras, S. (eds) Big Data in Engineering Applications. Studies in Big Data, vol 44. Springer, Singapore.  https://doi.org/10.1007/978-981-10-8476-8_13
 
 T. Adetiloye, A. Awasthi(2017). Predicting Short-Term Congested Traffic Flow on Urban Motorway Networks. 
     In P. Samui, S.S Roy, V.E. Balas(Eds.), Handbook of Neural Computation(pg. 145–165).
     doi: https://doi.org/10.1016/B978-0-12-811318-9.00008-9. Academic Press.

### LICENSE

 T. Adetiloye (2021). Predicting Short-Term Traffic Flow Congestion On Urban Motorway Networks (Patent No US11,195,412 B2).  U.S. Patent and Trademark Office. https://rb.gy/yaonm9
