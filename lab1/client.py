'''
################################## client.py #############################
# 
################################## client.py #############################
'''
import grpc
import datastore_pb2
import argparse
import random
import time
import uuid
import rocksdb
from decorator import Decorator
from concurrent.futures import ThreadPoolExecutor
PORT = 3000

class DatastoreClient():
        
    def __init__(self, host='0.0.0.0', port=PORT):        
        self.channel = grpc.insecure_channel('%s:%d' % (host, port))
        self.stub = datastore_pb2.DatastoreStub(self.channel)
        
           

    def put(self, value):
        return self.stub.put(datastore_pb2.Request(data=value))

    def get(self, key):
        return self.stub.get(datastore_pb2.Request(data=key))

    def send_stream_request(self, req):
        print('sending requests')
        return self.stub.StreamPutMethod(req)

    def get_stream_requests(self,req):
        print('geting response')
        return self.stub.StreamGetMethod(req)
          

def getResponse(key):   
        yield datastore_pb2.Stream_Request(data=key)
        
    

def sendRequests():
    reqs = [datastore_pb2.Stream_Request(data='MySQl'), datastore_pb2.Stream_Request(data='Aurora'),
            datastore_pb2.Stream_Request(data='PostGreSql'), datastore_pb2.Stream_Request(data='Redis'),
            datastore_pb2.Stream_Request(data='MongoDB')]
    while 1:
        for req in reqs:
            yield req
            time.sleep(random.uniform(2, 4)) 

def main():
    
    parser = argparse.ArgumentParser()
    parser.add_argument("host", help="display a square of a given number")
    args = parser.parse_args()
    print("Client is connecting to Server at {}:{}...".format(args.host, PORT))
    client = DatastoreClient(host=args.host)

    resp_key = client.send_stream_request(sendRequests())
    
    for key in resp_key:
        #print(res)
        final = str(key.data)
        val = client.get_stream_requests(getResponse(final))       
        for x in val:
            print(x.data)
                
        
    

    #value = 'foo'
    #print("## PUT Request: value = " + value) 
    #resp = client.put(value)
    #key = resp.data
    #print("## PUT Response: key = " + key)

    #print("## GET Request: key = " + key) 
    #resp = client.get(key)
    #print("## GET Response: value = " + resp.data) 


if __name__ == "__main__":
    main()

