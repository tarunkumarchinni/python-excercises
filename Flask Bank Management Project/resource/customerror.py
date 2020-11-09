from flask import jsonify
import json
from flask import Response


class InternalServerError(Exception):
    pass

class AccountAlreadyExistsError(Exception):
    pass
    
errors = {
    "InternalServerError": {
        "message": "Something went wrong",
        "status": 500
    },
     "SchemaValidationError": {
         "message": "Request is missing required fields",
         "status": 400
     },
     "AccountAlreadyExistsError": {
         "message": "Username already exists.please provide another!!",
         "status": 400
     }
}


    # def __init__(self,message):
    #     self.message=message
    # def __str__(self):
    #     return json.loads(self.message)
    # def __repr__(self):
    #     return self.__str__()
