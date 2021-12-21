from django.shortcuts import render
from dotenv import load_dotenv
import pyrebase
import os


load_dotenv()

firebaseConfig = {
  "apiKey": os.getenv('DEV_API_KEY'),
  "databaseURL": os.getenv('DEV_DATABASE_URL'),
  "authDomain": os.getenv('DEV_AUTH_DOMAIN'),
  "projectId": os.getenv('DEV_PROJECT_ID'),
  "storageBucket": os.getenv('DEV_STORAGE_BUCKET'),
  "messagingSenderId": os.getenv('DEV_MESSAGING_SENDER_ID'),
  "appId": os.getenv('DEV_APP_ID'),
}

print('firebaseConfig.databaseURL',firebaseConfig["databaseURL"])
print('firebaseConfig.apiKey',firebaseConfig["apiKey"])
# Firebase authentication
firebase = pyrebase.initialize_app(firebaseConfig)
authe = firebase.auth()
database = firebase.database()

def index(request):
        #accessing our firebase data and storing it in a variable
        name = database.child('Data').child('Name').get().val()
        stack = database.child('Data').child('Stack').get().val()
        framework = database.child('Data').child('Framework').get().val()

        context = {
            'name':name,
            'stack':stack,
            'framework':framework
        }

        return render(request, 'index.html', context)
