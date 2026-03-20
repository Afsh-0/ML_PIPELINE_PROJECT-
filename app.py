from flask import Flask
from src.logger import logging #we are calling an log.config
from src.exception import CustmeException
import os, sys

app = Flask(__name__) #we have created an object of an application

@app.route('/', methods = ['GET', 'POST'])
def index():
    try:
        raise Exception("We are testing our custom file")
    except Exception as e:
        abc = CustmeException(e, sys)
        logging.info(abc.error_message)
        return "welcome to basic pipeline ml project"
    

if __name__ == "__main__":
    app.run(debug=True)