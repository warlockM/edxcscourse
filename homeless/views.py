from django.shortcuts import render
import pandas as pd
import io
import urllib, base64
from .models import Contact
from django.http import HttpResponseRedirect
from django.urls import reverse
from . import util
# Create your views here.

states = ["Andhra-Pradesh", "Arunachal-Pradesh", "Assam", "Bihar", "Chhatisgarh",
        "Goa", "Gujarat", "Haryana", "Himachal-Pradesh", "Jharkhand", "Karnataka",
        "Karnataka", "Kerela", "Madhya-Pradesh", "Maharashtra", "Manipur", "Meghalaya",
        "Mizoram", "Nagaland", "Orissa", "Punjab", "Rajasthan", "Sikkim", "Tamil-Nadu",
        "Telangana", "Tripura", "Uttar-Pradesh", "Uttrakhand", "West-Bengal"
    ]

union_territories = ["Andaman&Nicobar", "Chandigarh", "Dadra&Nagar-Haveli",
    "Daman&Diu", "Delhi", "Jammu&Kashmir", "Lakshadweep", "Puducherry", "Laddakh"
    ]

def index(request):
    return render(request, "homeless/index.html")

def contact(request):
    return render(request, "homeless/contact.html")

def save_contact(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        purpose = request.POST["purpose"]

    data = Contact(name = name, email = email, purpose = purpose)
    #data.save()
    return render(request, "homeless/thanks.html", {
        "name": name
    })

def aboutus(request):
    return render(request, "homeless/aboutus.html")

def infra(request):
    return render(request, "homeless/infra.html")

def stateinfra(request, name):
    if name in states or union_territories:
        data = name
        return render(request, "homeless/stateinfra.html", {
        "data": data
        })
'''
def edu(request):
    if name in states or union_territories:
        data = name
        return render(request, "homeless/stateedu.html", {
        "data": data
        })

def health(request):
    if name in states or union_territories:
        data = name
        return render(request, "homeless/statehealth.html", {
        "data": data
        })
'''
