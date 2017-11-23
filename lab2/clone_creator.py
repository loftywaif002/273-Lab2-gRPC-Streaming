import rocksdb

class CreateReplica():

    def __init__(self):
        db1 = rocksdb.DB("replica1.db", rocksdb.Options(create_if_missing=True))
        db2 = rocksdb.DB("replica2.db", rocksdb.Options(create_if_missing=True))    
        db3 = rocksdb.DB("replica3.db", rocksdb.Options(create_if_missing=True))
    
    def get_data(key):
    	return self.db1.get(key)
 
    def put_data(key,data):
    	print("putting data in clone")
    	self.db1.put(key,data)

    def clone_db(self, data):
        db1 = rocksdb.DB("replica1.db", rocksdb.Options(create_if_missing=True))
        db2 = rocksdb.DB("replica2.db", rocksdb.Options(create_if_missing=True))    
        db3 = rocksdb.DB("replica3.db", rocksdb.Options(create_if_missing=True))
        print("data is passed!")
        print("key is "+ str(self))  	
        print("data is "+ str(data))
        print("clonng this data into replicas using same key,value")
        key = self.encode('utf-8')
        encoded_data = data.encode('utf-8')
        db1.put(key,encoded_data)
        db2.put(key,encoded_data)
        db3.put(key,encoded_data)
        print("getting data from clone1")
        print(db1.get(key))
        print("getting data from clone1")
        print(db2.get(key))
        print("getting data from clone1")
        print(db3.get(key))


	    

    


	
