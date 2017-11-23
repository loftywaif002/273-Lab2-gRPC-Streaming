'''
################################## server.py #############################
# Lab1 gRPC RocksDB Server 
################################## server.py #############################
'''
import time
import grpc
import datastore_pb2
import datastore_pb2_grpc
import uuid
import rocksdb



from concurrent import futures

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class MyDatastoreServicer(datastore_pb2.DatastoreServicer):
    def __init__(self):
        self.db = rocksdb.DB("master.db", rocksdb.Options(create_if_missing=True))      
    
            
    def put(self, request, context):
        print("put")
        key = uuid.uuid4().hex
        key = key.encode("utf-8")
        s = request.data
        s = s.encode("utf-8")
        self.db.put(key, s)
        print(request) 
        # TODO - save key and value into DB converting request.data string to utf-8 bytes 
        
        return datastore_pb2.Response(data=key)

    def get(self, request, context):
        print("get")
        print(request)
        # TODO - retrieve the value from DB by the given key. Needs to convert request.data string to utf-8 bytes. 
        value = self.db.get(request.data.encode("utf-8"))

        return datastore_pb2.Response(data=value)

    def StreamPutMethod(self, request_iterator, context):
        for req in request_iterator:
            print("inside put method")
            print(req.data)
            key = uuid.uuid4().hex
            key = key.encode("utf-8")
            s = req.data
            s = s.encode("utf-8")
            self.db.put(key, s)
            yield datastore_pb2.Stream_Response(data=key)

    def StreamGetMethod(self, request_iterator, context):
        for req in request_iterator:
            print("inside get method")
            s = req.data.encode("utf-8")
            value = self.db.get(s)
            val=value.decode('utf-8')
            print(val)
            yield datastore_pb2.Stream_Response(data=value)
    
def run(host, port):
    '''
    Run the GRPC server
    '''
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    datastore_pb2_grpc.add_DatastoreServicer_to_server(MyDatastoreServicer(), server)
    server.add_insecure_port('%s:%d' % (host, port))
    server.start()
    
    try:
        while True:
            print("Server started at...%d" % port)
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    run('0.0.0.0', 3000)