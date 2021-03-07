from django.db import models
from django.shortcuts import render
from .models import Listing
from .models import *


def index(request):
    return render(request, 'listings/listings.html', {
        'name': 'NabiL'
    })


def listing(request):
    return render(request, 'listings/listing.html')


def search(request):
    return render(request, 'listings/search.html')
