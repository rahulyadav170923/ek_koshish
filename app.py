from flask import Flask,render_template,request,url_for,jsonify,json,session,redirect

import unirest
import httplib
from parse_rest.connection import register
register(<application_id>, <rest_api_key>[, master_key=None]) //parse credentials
from parse_rest.datatypes import Object
app=Flask(__name__)

class ngos(Object):
    pass


class resource(Object):
    pass



class user(Object):
    pass



headers={
  "X-Parse-Application-Id": "----",
  "X-Parse-REST-API-Key": "-------",
  "Content-Type": "application/json"
  }


// ngo info
@app.route('/ngolist',methods=['GET'])
def ngolist():
    connection = httplib.HTTPSConnection('api.parse.com', 443)
    connection.connect()
    connection.request('GET', '/1/classes/ngos', '',headers)
    result = json.loads(connection.getresponse().read())
    return jsonify(result)

// userinfo
@app.route('/userlist',methods=['GET'])
def userlist():
    connection = httplib.HTTPSConnection('api.parse.com', 443)
    connection.connect()
    connection.request('GET', '/1/classes/users', '',headers)
    result = json.loads(connection.getresponse().read())
    return jsonify(result)

//resource_requests info

@app.route('/resources',methods=['GET'])
def resources():
    connection = httplib.HTTPSConnection('api.parse.com', 443)
    connection.connect()
    connection.request('GET', '/1/classes/resource', '',headers)
    result = json.loads(connection.getresponse().read())
    return jsonify(result)

@app.route('/<ngoname>/pending_requests',methods=['GET'])
def pending_requests():
    response=ngo_pending_request()
    return render_template('index.html',response=response)

@app.route('/<ngoname>/accepted_requests',methods=['GET'])
def accepted_requests():
    response=ngo_accepted_request()
    return render_template('index.html',response=response)

@app.route('/<user_id>/requests',methods=['GET'])
def total_requests():
    total_requests=user_requests
    return jsonify(total_requests)

def ngo_pending_request(ngo_id):
    requests=user.Query.get(objectId=ngo_id)
    dict=[]
    for i in requests:
        pending_request=i.Query.filter(request_accepted=False)
        dict.append(pending_request)
    return dict


def ngo_accepted_request(ngo_id):
    requests=user.Query.get(objectId=ngo_id)
    dict=[]
    for i in requests:
        accepted_requests=i.Query.filter(request_accepted=True)
        dict.append(accepted_request_request)
    return dict

def user_requests(user_id):
    requests=user.Query.get(objectId=user_id)
    return requests






if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')
