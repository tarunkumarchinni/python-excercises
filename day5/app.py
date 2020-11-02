#code
from flask import Flask,request
app = Flask(__name__)

customerList={
    1:{"Name":"arjun","Username":"tc123","Password":"pass@123","Address":"5-6-1/1, ring road","State":"AP","Country":"india","Email":"arjun@gmail.com","Pan":"6537le2","Contact":"8897675611","DOB":"10-4-1992","Accounttype":"savings"},
    2:{"Name":"arvind","Username":"avc123","Password":"pass@123","Address":"5-6-1/1, ring road2","State":"AP","Country":"india","Email":"arvind@gmail.com","Pan":"5437le2","Contact":"7797675611","DOB":"1-2-1995","Accounttype":"credit"},
    3:{"Name":"raj","Username":"raj123","Password":"pass@123","Address":"5-6-1/1, ring road3","State":"AP","Country":"india","Email":"raj@gmail.com","Pan":"3237le2","Contact":"6697675611","DOB":"5-12-2000","Accounttype":"current"}
}

@app.route('/')
def basic():
    return "welcome to the bank management system"

@app.route('/register',methods=['POST','GET'])
def registerCustomer():
    if request.method == 'POST':
        new_customer=request.json
        x=False
        for i in customerList:
            if customerList[i]["Username"] == new_customer["Username"]:
                x=True
        if x:
            return "user already exists"
        else:
            # customer=request.json
            #mongodb code
            id=max(customerList)+1
            customerList[id]=new_customer
            return customerList[id],201
    else:
        #mongodb to get all the customers
        return customerList,200

# @app.route('/applyloan',methods=['POST','GET'])
# def applyLoan():
#     if request.method == 'POST':
#         #mongo db code to insert the application details of loan
#     else:
#         #customer applyed status of loans particular to that customer

@app.route('/updateaccount/<customer_id>',methods=['PUT', 'GET', 'DELETE'])
def accountUpdate(customer_id):
    x=False
    for i in customerList:
        if customerList[i]["Username"] == customer_id:
            x=True
    if x:
        if request.method == 'PUT':
            #update the details in mongodb
                new_customer=request.json
                for i in customerList:
                    if customerList[i]["Username"] == customer_id:
                        customerList[i]=new_customer
                        y=i
                return customerList[y],201
        elif request.method == 'DELETE':
            #delete the details in mongodb
            # new_customer=request.json
            for i in customerList:
                if customerList[i]["Username"] == customer_id:
                    y=i
            del customerList[y]
            return customerList,201
        else:
            #get the updated details of single resource
            for i in customerList:
                if customerList[i]["Username"] == customer_id:
                    y=i
            return customerList[y],200
    else:
        #customer not found
        return "user does not exists to update",404


# @app.route('/login/<username>',methods=['GET'])
# def login():
#     #check if the user is in db
#     if user exists:
#         #able to access system redirects to apply loan
#     else:
#         #not a registered user. redirects to login


if __name__=="__main__":
    app.run(debug=True)