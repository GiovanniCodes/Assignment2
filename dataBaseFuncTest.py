import pymongo
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError



class databaseNeedStub:
    @staticmethod
    def connection():

        client2 = pymongo.MongoClient()

        if (client2):
            return True
        else:
            print("server is down.")
            return False


    @staticmethod
    def printStubData(x):

            return 10





