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
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=['GET','POST'])
def contact():
    if request.method == "POST":
        #Do something with data
        print(request.form)
        return render_template("contact.html")

    return render_template("contact.html")

@app.route("/demo", methods=['GET','POST'])
def demo():
    return render_template("demo.html")


@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500


if __name__ == '__main__':
    # app.run(debug=True, use_reloader=True)
     # This is used when running locally. Gunicorn is used to run the
     # app on Google App Engine. See entrypoint in app.yaml.
     #app.run(debug=True, use_reloader=True)
     app.run(debug=True, host='0.0.0.0', port=8001)