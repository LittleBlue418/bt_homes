from django.shortcuts import render

from listings.models import Listing
from realtors.models import Realtor


"""
    Using the Listings model to import listings for the front page.
    Filtered by the most recent, only published, and only returning
    3 listings.
"""
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = {
        'listings': listings
    }

    return render(request, 'pages/index.html', context)


"""
    Using the Realtors model to import data about all realtors for the
    about page.
    Filtering the realtors by mvp to also return the mvp realtors (seller
    of the month)
"""
def about(request):
    realtors = Realtor.objects.order_by('-hire_date')

    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }

    return render(request, 'pages/about.html', context)
