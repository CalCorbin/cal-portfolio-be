from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TodoSerializer
from .models import Todo
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

# Firebase authentication

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
database = firebase.database()


class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
