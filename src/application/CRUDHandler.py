import traceback
import json

from pymongo import MongoClient
from pymongo.errors import WriteConcernError, WriteError


class CRUDHandler:
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username: str, password: str):
        """ initialize mongoClient. This method overrides a magic method from the Object class """

        # create MongoClient to connect to MongoDB, using authentication
        self.client = MongoClient('mongodb://%s:%s@localhost:27017/AAC' % (username, password))
        self.collection = self.client['AAC']["animals"]

    def create(self, doc_to_insert: dict) -> bool:
        """ C in CRUD """

        inserted = False
        if doc_to_insert is not None:
            # insert the document into AAC.animals collection
            self.collection.insert_one(doc_to_insert)  # data should be dictionary
            inserted = True

        else:
            raise Exception("Nothing to save, data parameter empty")

        return inserted

    def findDocs(self, search_criteria: dict):
        """ R in CRUD """

        if search_criteria is not None:
            # search AAC.animals for specific values
            results = self.collection.find(search_criteria)
            #             for document in results:
            #                 print(document["_id"])
            return results

        else:
            raise Exception("Something went wrong. Check the search criteria and try again")

    def update(self, look_up_values: dict, new_values: dict):
        """ U in CRUD """

        result = None
        try:

            # if arguments were not null
            if look_up_values is not None and new_values is not None:

                # try updating the document that matches the criteria
                result = self.collection.update_one(look_up_values, {"$set": new_values})

                # if the update_one function was successful, return true
                if result.modified_count != 0:
                    print("Successfully updated document")

                else:
                    print("Failed to update document")

                # return json object
                json_object = json.dumps(result.raw_result, indent=4)
                return json_object

            else:
                raise Exception("look up values or update values were not specified")

        # if an update error occurred, return the error
        except WriteConcernError as wce:
            print("A WriteConcernError occurred")
            return wce
        except WriteError as we:
            print("A WriteError occurred")
            return we
        except:
            print("An error occurred when trying to update the document")
            traceback.print_exc()

    def delete(self, doc_to_delete: dict):
        """ D in CRUD """

        try:
            # if argument was not null
            if doc_to_delete is not None:
                # try to delete a document in the database with the argument values
                result = self.collection.delete_one(doc_to_delete)

                # return json version of deleted object only if delete count was not 0
                if result.deleted_count > 0:
                    print("Deletion successful")

                else:
                    print("Failed to delete document")

                # return json object
                json_object = json.dumps(result.raw_result, indent=4)
                return json_object

            else:
                raise Exception("doc_to_delete variable was null")

        # if a deletion error occurred, return the error
        except WriteConcernError as wce:
            print("A WriteConcernError occurred")
            return wce
        except WriteError as we:
            print("A WriteError occurred")
            return we
        except:
            print("An error ocurred when trying to delete the document")
            traceback.print_exc()
