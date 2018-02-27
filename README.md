# TensorflowPredictCongestTypes
Python tensorflow is used to predict the congestion types based on image object recognition

**HOW TO TEST**

**1. Clone git repository and `cd` into the directory**

     git clone https://github.com/taiwotman/TensorflowPredictCongestTypes.git

**2. Set up virtualevn with directory _venv_** 

     virtualevn venv

**3. Activate _venv_ using:**

     source venv/bin/activate

**4. Install tensorflow using:**

     pip install tensorflow

**5. Use  traffic congestion images(supports only jpeg/jpg format). For example:**

     python run.py test_image/Aut10_010.jpg
     
**6. Example output:**

      high congestion (score = 0.70454)

**TODO**

Create Flask REST API consuming (real-time) traffic image  data for prediction.

**You want to be a contributor?** 
1. Fork repository

     and/or

2. Connect and chat me on [LinkedIn](https://www.linkedin.com/in/taiwo-o-adetiloye-505a8023/).
