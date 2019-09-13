# Using Tensorflow to Predict Traffic Congestion Types.
Python tensorflow is used to predict the congestion types based on image object recognition
 
<p align="center"> 
 <img width="200" height="200" src="https://github.com/taiwotman/TensorflowPredictCongestionTypes/blob/master/miscellanous/smart-traffic.png"></p>
 <p align="center">
<img width="200" height="200" src="https://github.com/taiwotman/TensorflowPredictCongestionTypes/blob/master/miscellanous/high-congestion.png">
 <img width="200" height="200" src="https://github.com/taiwotman/TensorflowPredictCongestionTypes/blob/master/miscellanous/medium-congestion.png">
 <img width="200" height="200" src="https://github.com/taiwotman/TensorflowPredictCongestionTypes/blob/master/miscellanous/low-congestion.png">
</p>

**HOW TO TEST**

**1. Clone git repository and `cd` into the directory**

     git clone https://github.com/taiwotman/TensorflowPredictCongestionTypes.git
     
     cd TensorflowPredictCongestionTypes

**2. Set up [virtualenv](https://virtualenv.pypa.io/en/stable/) with directory _venv_** 

     virtualenv venv

**3. Activate _venv_ using:**

     source venv/bin/activate

**4. Install [tensorflow](https://www.tensorflow.org) using:**

     pip install tensorflow

**5. Use  traffic congestion image(supports only jpeg/jpg format). For example:**

     python run.py test_image/Aut10_010.jpg
     
**6. Example output:**

      high congestion (score = 0.70454)
      
**Docker:** 

https://hub.docker.com/r/taiwotman/smart-traffic

Flask REST API using (real-time) traffic image  data for prediction.


**You want to be a contributor?** 
1. Fork repository

     and/or

2. Connect and chat me on [LinkedIn](https://www.linkedin.com/in/taiwo-o-adetiloye-ph-d-505a8023/).

**FOR ACADEMIC PURPOSE; 
kindly, cite our related work:**
     
     T. Adetiloye, A. Awasthi  (2019). Multimodal Big Data Fusion for Traffic Congestion Prediction. 
         In: Seng K., Ang L., Liew   AC., Gao J. (eds) Multimodal Analytics for Next-Generation Big Data Technologies 
         and Applications(pg. 319-335). doi: https://doi.org/10.1007/978-3-319-97598-6_13Springer. Springer, Cham.
     
     
     T. Adetiloye, A. Awasthi(2017). Predicting Short-Term Congested Traffic Flow on Urban Motorway Networks. 
          In P. Samui, S.S Roy, V.E. Balas(Eds.), Handbook of Neural Computation(pg. 145–165).
          doi: https://doi.org/10.1016/B978-0-12-811318-9.00008-9 . Academic Press.

     


