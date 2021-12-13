# Predicting Short-Term Traffic Flow Congestion On Urban Motorway Networks


**RELEASE 2.1.1**

- Create Flask REST API using (real-time) traffic image  data for prediction.

- Implement search query on the basis on region
      
- Make Jinja template to display parameters on index.page 

- On Index page display image with URL while adding dropdown or selection with regions

- Clean template
      
- Add Prediction features


**HOW TO TEST**

**1. Clone git repository and `cd` into the directory**

     git clone https://github.com/taiwotman/TensorflowPredictCongestionTypes.git
     
     cd TensorflowPredictCongestionTypes

**2. Set up [virtualenv](https://virtualenv.pypa.io/en/stable/) with directory _venv_** 

     virtualenv venv

**3. Activate _venv_ using:**

     source venv/bin/activate

**4. Install [tensorflow](https://www.tensorflow.org) and others using:**

     pip install -r requirements.txt

**5. Use  traffic congestion image(supports only jpeg/jpg format). For example:**

     python run.py test_image/Aut10_010.jpg
     
**6. Example output:**

      high congestion (score = 0.70454)
 
      
## Using Docker

#### docker build -t taiwotman/smart-traffic:latest .

#### docker run --rm -p 80:5000 taiwotman/smart-traffic:latest 

### AWS EKS

kubectl apply -f aws_eks/deployment.yaml smart-traffic-service created deployment.apps/smart-traffic created

http://localhost:8080/api/v1/namespaces/default/services/smart-traffic-service/proxy
     
eksctl delete cluster --region=us-east-2 --name=smart-cluster


## Deploy app on google cloud engine

     gcloud app deploy

**PS:** _deploy might take several minutes_

if error on starting reinitialize project using:

     gcloud app init

**if error**

     ERROR: (gcloud.app.deploy) INVALID_ARGUMENT: unable to resolve source

Go to storage bucket and delete app storage.

Then redeploy app.


**You want to be a contributor?** 
1. Fork repository

     and/or

2. Connect and chat me on [LinkedIn](https://www.linkedin.com/in/taiwo-o-adetiloye-505a8023/).

**FOR ACADEMIC PURPOSE; kindly, cite our related work:**

     , A. Awasthi(2017). Predicting Short-Term Congested Traffic Flow on Urban Motorway Networks. 
     In P. Samui, S.S Roy, V.E. Balas(Eds.), Handbook of Neural Computation(pg. 145–165).
     doi: https://doi.org/10.1016/B978-0-12-811318-9.00008-9 . Academic Press.

**COMMERCIAL USE, UNDER PATENT LICENCE**

      T. Adetiloye (2021). Predicting Short-Term Traffic Flow Congestion On Urban Motorway Networks (Patent No US11,195,412 B2). U.S. Patent and Trademark Office. 
      https://rb.gy/faqg9y
