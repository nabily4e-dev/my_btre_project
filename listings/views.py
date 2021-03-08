from django.shortcuts import render, get_object_or_404
from .models import Listing
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import state_choices, bedrooms_choices, price_choices


def index(request):

    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {'listings': paged_listings}

    return render(
        request,
        'listings/listings.html',
        context,
    )


def listing(request, listing_id):
    """"""

    listing = get_object_or_404(
        Listing,
        pk=listing_id,
    )

    context = {
        'listing': listing,
    }

    return render(
        request,
        'listings/listing.html',
        context,
    )


def search(request):
    """"""

    query_list = Listing.objects.order_by('-list_date')

    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            query_list = query_list.filter(description__icontains=keywords)

    # City
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            query_list = query_list.filter(city__iexact=city)
            
    # State
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            query_list = query_list.filter(state__iexact=state)


    context = {
        'state_choices': state_choices,
        'bedroom_choices': bedrooms_choices,
        'price_choices': price_choices,
        'listings': query_list,
    }

    return render(
        request,
        'listings/search.html',
        context,
    )
