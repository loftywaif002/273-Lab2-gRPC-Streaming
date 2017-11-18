import rocksdb

class Decorator():
    def __init__(self):
        self.db1 = rocksdb.DB("replica1.db", rocksdb.Options(create_if_missing=True))
        self.db2 = rocksdb.DB("replica2.db", rocksdb.Options(create_if_missing=True))    
        self.db3 = rocksdb.DB("replica3.db", rocksdb.Options(create_if_missing=True))

    def clone_db(self,key):
	    temp1 = self.db1.get(key)
	    temp2 = self.db2.get(key)
	    temp3 = self.db3.get(key)
	    print(temp1)
	    print(temp2)
	    print(temp3)

	
	
