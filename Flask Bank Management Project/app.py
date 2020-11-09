import json
import requests
from flask import Flask, request, jsonify
from model.db import initilaize_db
from resource.accountsapi import account_api
from resource.loanapi import loan_api
from resource.customerror import errors

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'db': 'accountsdb',
    'host': 'mongodb://localhost:27017/accountsdb',
    
}

# app.config['PROPAGATE_EXCEPTIONS'] = False

# @app.errorhandler(404) 
# def not_found(error): 
#     return make_response(jsonify({'error': 'Not found'}), 404)

initilaize_db(app)
account_api(app,errors=errors)
loan_api(app)

# url_request="http://127.0.0.1:5050/"


@app.route('/')
def basic():
    # respon = requests.get(url_request2+'/user')
    # print(respon.json())
    return "welcome user"

if __name__ == "__main__":
    app.run(debug=True)