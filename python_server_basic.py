from flask import Flask
from flask_restful import Api, Resource
from http.server import BaseHTTPRequestHandler, HTTPServer
import requests

app = Flask(__name__)
api = Api(app)

# session = requests.Session()

# ips of the mini miners at hunterville
ips = {
        "192.168.1.57", 
        "192.168.1.16", 
        "192.168.1.163", 
        "192.168.1.28",
        "10.0.0.141",
        "10.0.0.176" 
        }

# Getting json data from miners
def GetData():
    minerData = []
    for ip in ips:
# add status wich include primarly type of miner and version
        try:
                r = requests.get(f"http://{ip}/mcb/status")
                status = {"status" : [r.json()]}
        except:
                status = {"status" : "error"}


# add all data that asinc miner has
        try:
                r = requests.get(f"http://{ip}/mcb/cgminer?cgminercmd=devs")
                data = { "data" : [r.json()]}

        except:
                status = {"status" : "error"}

        

        minerData.append( [{"ip" : ip}, status, data])
    return minerData

class Miner_Data_Api(Resource):
        def get(self): 
                return GetData()




api.add_resource(Miner_Data_Api, "/miner_data")

if __name__ == "__main__":        
  app.run()
