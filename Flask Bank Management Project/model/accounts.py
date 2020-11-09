from model.db import db

class Accounts(db.Document):
    name=db.StringField(required=True)
    username=db.StringField(required=True,Unique=True)
    password=db.StringField(required=True)
    address=db.StringField(required=True)
    state=db.StringField(required=True)
    country=db.StringField(required=True)
    email=db.StringField(required=True)
    pan=db.StringField(required=True)
    contact=db.StringField(required=True)
    DOB=db.StringField(required=True)
    accounttype=db.StringField(required=True)