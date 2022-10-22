from flask import Flask,request, jsonify, Response
import json
from flask_cors import CORS

app = Flask('__main__', template_folder='./')

CORS(app)

host_ip = "127.0.0.1"

host_port = 5000

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin','*')
    response.headers.add('Access-Control-Allow-Headers','Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods','GET,PUT,POST,DELETE,OPTIONS')
    return response


@app.route('/', methods = ['POST','GET'])
def index():
    return 'home'

@app.route('/api/v1/save',methods = ['POST'])
def save_co_ord():
       
        data = json.loads(request.data)
        print(data['File'])
        f = open("Co_ordinates.json", "a")
        json.dump(data,f)
        f.close()
        response = jsonify({})
        
        return response, 201

if __name__ == "__main__":
    app.run(host = host_ip, port = host_port)
