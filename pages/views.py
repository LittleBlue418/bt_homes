from django.shortcuts import render

from listings.models import Listing


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

def about(request):
    return render(request, 'pages/about.html')
