# Using Tensorflow to Predict Traffic Congestion Types.
Python tensorflow is used to predict the congestion types based on image object recognition

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

**TO DO**

Create Flask REST API using (real-time) traffic image  data for prediction.

Implement search query on the basis on region
      
Make Jinja template to display parameters on index.page 

On Index page display image with URL while adding dropdown or selection with regions

Clean template
      
Add Prediction features
 
 Add schedule to update/refresh page
      
      
**You want to be a contributor?** 
1. Fork repository

     and/or

2. Connect and chat me on [LinkedIn](https://www.linkedin.com/in/taiwo-o-adetiloye-505a8023/).

**FOR ACADEMIC PURPOSE; kindly, cite our related work:**

     T. Adetiloye, A. Awasthi(2017). Predicting Short-Term Congested Traffic Flow on Urban Motorway Networks. 
     In P. Samui, S.S Roy, V.E. Balas(Eds.), Handbook of Neural Computation(pg. 145–165).
     doi: https://doi.org/10.1016/B978-0-12-811318-9.00008-9 . Academic Press.

3. Deploy app on google cloud engine

      **gcloud app deploy**

      **PS:** _deploy might take several minutes_

      if error on starting reinitialize project using:

      **gcloud app init**

      **if this error**

            ERROR: (gcloud.app.deploy) INVALID_ARGUMENT: unable to resolve source

      Go to storage bucket and delete all storage.

      Then redeploy you app.

## Using Docker

#### docker build -t taiwotman/smart-traffic:latest .

#### docker run --rm -p 80:5000 taiwotman/smart-traffic:latest 