from django.shortcuts import render
from .models import person_collection
from django.http import HttpResponse

def index(request):
    return HttpResponse("APP is running.")
# Create your views here.
def add_person(request):
    records = {
        "first_name": "dhruvil",
        "last_name": "shah"
    }

    person_collection.insert_one(records)
    return HttpResponse("new person added")

def get_all_person(request):
    persons = person_collection.find()
    return HttpResponse(persons)


