"""
Author: Taiwo O. Adetiloye
Date: August 18, 2018
"""


import json
from predictor import predict
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import http.client as httplib
from urllib.request import Request, urlopen  # Python 3



def get_traffic(query):
    
    try:
            headers= {
                "Authorization": "************,
                "Connection": "keep-alive" 
            }

            featureJson = {

                    "properties": {
                        "region": query,
                    }
                }

            region = featureJson['properties']['region']
            
            url = 'https://api.transport.nsw.gov.au/v1/live/cameras'
        
            request = Request(url, None,headers)
            
            data= urlopen(request).read()
        
            features = json.loads(data).get('features')
            traffic = []  

            for feature in features:
                response = feature['properties']
                if response.get("region") ==None or response.get("region") == "": 
                    pass
                if response.get("region") == region:
                    
                    traffic.append({"region":response["region"],"title":response["title"],"view":response["view"],
                        "direction":response["direction"],"href":response["href"], "predict":predict.tensorflow_pred(response["href"])}) 
            
            return traffic
     # DO STUFF
    except httplib.BadStatusLine:
        pass          
