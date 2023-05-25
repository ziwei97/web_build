import pymysql
from flask import Flask,request,jsonify
from flask_cors import CORS
import gevent
from gevent import pywsgi

conn = pymysql.connect(host="127.0.0.1",user="root",password="szw970727",db="algorithm")
cursor = conn.cursor()

app = Flask(__name__)
CORS(app,resources=r'/*')


@app.route('/url',methods=["POST"])
def func():
    if request.method=="POST":
        ImgCollGUID = request.form.get("ImgCollGUID")
        print("get GUID: "+str(ImgCollGUID))
        return "return to front side"

@app.route('/login/list',methods=["POST"])
def login_list():
    if request.method=="POST":
        cursor.execute("SELECT ImgCollGUID,Bucket,Wound,SubjectID from results")
        data = cursor.fetchall()
        temp = {}
        result=[]
        if(data!=None):
            for i in data:
                temp["GUID"]=i[0]
                temp["SubjectID"]=i[3]
                result.append(temp.copy())
            return jsonify(result)
        else:
            print("no results")
            return jsonify([])


if __name__ =="__main__":
    server = pywsgi.WSGIServer(('',8899),app)
    # app.run(host='0.0.0.0',port=8899)
    server.serve_forever()
    conn.close()
    print("good bye!")