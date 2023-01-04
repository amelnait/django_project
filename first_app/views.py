# connect to mongodb
import json
from django.http import HttpResponse

from pymongo import MongoClient
def index(request):
    return HttpResponse("Hello, world. You're at the index.")
import requests
url="https://odre.opendatasoft.com/api/records/1.0/search/?dataset=prod-nat-gaz-horaire-prov&q=&rows=10000&sort=journee_gaziere&timezone=Europe%2FParis"
r=requests.get(url)
#r=requests.get('https://opendata.paris.fr/api/records/1.0/search/?dataset=velib-disponibilite-en-temps-reel&rows=1000&facet=name&facet=is_installed&facet=is_renting&facet=is_returning&facet=nom_arrondissement_communes&facet=coverflow&facet=creditcard&facet=overflowactivation&facet=kioskstate&facet=station_state')
velib=r.json()
#print(velib)
def get_database():
 
   # Provide the mongodb atlas url to connect python to mongodb using pymongo
   CONNECTION_STRING = "mongodb+srv://linux_site_web:o0uh950JLuOCL8Ww@cluster0.3iix0gl.mongodb.net/test?retryWrites=true&w=majority"
 
   # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
   client = MongoClient(CONNECTION_STRING)
 
   # Create the database for our example (we will use the same database throughout the tutorial
   return client['test']

dbname = get_database()
"""with open('velib.json') as f:
    file_data = json.load(f)
"""
# find all the documents in the collection
dbname.test_collection.find()

#delete all the documents in the collection
dbname.test_collection.delete_many({})


#for i in velib["records"]:
dbname.test_collection.insert_many(velib["records"])
    


"""from django.shortcuts import render

from django.http import HttpResponse

from pymongo import MongoClient
def index(request):
    return HttpResponse("Hello, world. You're at the index.")

try:
    client=MongoClient('mongodb+srv://linux_site_web:o0uh950JLCL8Ww@cluster0.3iix0gl.mongodb.net/test?retryWrites=true&w=majority')
    print("Connected successfully!!!")
except :
    print("Could not connect to MongoDB")
    
dbname = client['test']

# Now get/create collection name (remember that you will see the database in your mongodb cluster only after you create a collection
collection_name = dbname["test_collection"]
#print(collection_name)

med_details = collection_name.find( )
# Print on the terminal
for r in med_details:
    print(r["_id"])
"""