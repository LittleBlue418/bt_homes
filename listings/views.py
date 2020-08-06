from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .choices import price_choices, bedroom_choices, state_choices
from .models import Listing


"""
    Returning all our house listings, ordered by the most recently
    published, filtered to only show published properties.

    Pagination used to display 6 to a page.
"""
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings,
    }

    return render(request, 'listings/listings.html', context)


"""
    Method for the single listing page. Returns a single listing using the listing id
    (as the primary key) passed in when a link / button is clicked; or a 404 page if not found.
"""
def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing': listing
    }

    return render(request, 'listings/listing.html', context)

def search(request):

    context = {
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices
    }

    return render(request, 'listings/search.html', context)
