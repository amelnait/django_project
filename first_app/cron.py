import json
from django.http import HttpResponse
import requests
from pymongo import MongoClient
from django_cron import CronJobBase, Schedule
from django_crontab.crontab import Crontab
import fcntl


def get_database():
        # Provide the mongodb atlas url to connect python to mongodb using pymongo
        CONNECTION_STRING = "mongodb+srv://linux_site_web:o0uh950JLuOCL8Ww@cluster0.3iix0gl.mongodb.net/test?retryWrites=true&w=majority"
        
        # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
        client = MongoClient(CONNECTION_STRING)
        
        # Create the database for our example (we will use the same database throughout the tutorial
        return client['test']
    
def MyCronJob():
    print("hello")
    url="https://opendata.paris.fr/api/records/1.0/search/?dataset=velib-disponibilite-en-temps-reel&q=&facet=name&facet=is_installed&facet=is_renting&facet=is_returning&facet=nom_arrondissement_communes&timezone=Europe%2FParis"
    r=requests.get(url)
    velib=r.json()

    dbname = get_database()
    dbname.test_collection.find()
    # find all the documents in the collection
    dbname.test_collection.find()

    #delete all the documents in the collection
    dbname.test_collection.delete_many({})
    dbname.test_collection.insert_many(velib["records"])
    

    
    
   