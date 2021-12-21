from django.shortcuts import render
from dotenv import load_dotenv
import pyrebase
import os


load_dotenv()

firebaseConfig = {
  "apiKey": os.getenv('DEV_APIKEY'),
  "databaseURL": os.getenv('DEV_DATABASEURL'),
  "authDomain": os.getenv('DEV_AUTHDOMAIN'),
  "projectId": os.getenv('DEV_PROJECTID'),
  "storageBucket": os.getenv('DEV_STORAGEBUCKET'),
  "messagingSenderId": os.getenv('DEV_MESSAGINGSENDERID'),
  "appId": os.getenv('DEV_APPID'),
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
