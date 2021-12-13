"""
Author: Taiwo O. Adetiloye
Date: August 22, 2018
"""

from flask import Flask,render_template,request, flash
import json
from json_parser import traffic_parser
import logging
from predictor import predict

app = Flask(__name__)

app.config['DEBUG'] = True

# change this to your own value 
app.secret_key = '*****'

@app.route("/")
def index():
    
    region = request.args.get('region')
    
    # if not region:
    #     region= DEFAULTS['region']
      
    traffic = traffic_parser.get_traffic(region)
    return render_template("home.html", traffic_properties = traffic, region=region)

@app.route("/about")
def about():
    return render_template("about.html")


@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500


@app.route('/contact', methods=['GET', 'POST'])
def contact():
  # form = ContactForm()

 

  if request.method == 'POST':

        return render_template('contact.html', success=True)

  elif request.method == 'GET':
    return render_template('contact.html', success=True)



if __name__ == '__main__':
    # app.run(debug=True, use_reloader=True)
     # This is used when running locally. Gunicorn is used to run the
     # app on Google App Engine. See entrypoint in app.yaml.
     #app.run(debug=True, use_reloader=True)
     app.run(debug=True, host='0.0.0.0', port=5000)
    


