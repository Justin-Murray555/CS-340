from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelterCRUD(object):
    """CRUD operations for Animal collection in MongoDB"""
    
    def __init__(self, username, password, host, port, database, collection):
        #Initalizing MongoClient
        USER = username
        PASS = password
        HOST = host
        PORT = port
        DB = database
        COL = collection
        
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        database = client['%s' % (DB)]
        collection = database['%s' % (COL)]
        
    def create(self, data):
        """Insert a document into MongoDB"""
        try:
            result = self.collection.insert_one(data)
            return True if result.inserted_id else False
        except Exception as e:
            print(f"Error inserting document: {e}")
            return False
        
    def read(self, query):
        try:
            cursor = self.collection.find(query)
            return list(cursor)
        except Exception as e:
            print(f"Error querying documents: {e}")
            return[]

    def update(self, query, new_data):
      """Update document in MongoDB"""
      try:
        result = self.collection.update_many(query, {'$set': new_data})
        return result.modified_count
      except Exception as e:
        print(f"An error occured: {e}")
        return 0
      
    def delete(self, query):
      """Delete document in MongoDB"""
      try:
        result = self.collection.delete_many(query)
        return result.deleted_count
      except Exception as e:
        print(f"An error occured: {e}")
        return 0
      
    
