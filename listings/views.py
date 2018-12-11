from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import price_choices, bedroom_choices, province_choices

# Bring in Listing model
from .models import Listing

# Dynamic view of listings from DB - fetch from model and loop through
def index(request):
  listings = Listing.objects.order_by('-list_date').filter(is_published=True)

  paginator = Paginator(listings, 6)
  page = request.GET.get('page')
  paged_listings = paginator.get_page(page)

  context = {
    'listings': paged_listings
  }

  return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
  listing = get_object_or_404(Listing, pk=listing_id)

  context = {
    'listing': listing
  }

  return render(request, 'listings/listing.html', context)

def search(request):
  # Search Filtering
  queryset_list = Listing.objects.order_by('-list_date')

  # Keywords
  if 'keywords' in request.GET:
    keywords = request.GET['keywords']
    if keywords:
      # Search description for any words typed into keyword box (Western Cape = Western Cape)
      queryset_list = queryset_list.filter(description__icontains=keywords)

  # City
  if 'city' in request.GET:
    city = request.GET['city']
    if city:
      # Search city - not case sensitive (iexact) 
      queryset_list = queryset_list.filter(city__iexact=city)

  # Province
  if 'province' in request.GET:
    province = request.GET['province']
    if province:
      # Search province - not case sensitive (iexact) 
      queryset_list = queryset_list.filter(province__iexact=province)

  # Bedrooms
  if 'bedrooms' in request.GET:
    bedrooms = request.GET['bedrooms']
    if bedrooms:
      # Get everything UP TO amount of bedrooms in search
      queryset_list = queryset_list.filter(bedrooms__gte=bedrooms)

  # Price
  if 'price' in request.GET:
    price = request.GET['price']
    if price:
      # Get everything UP TO amount of price in search
      queryset_list = queryset_list.filter(price__lte=price)

  context = {
    'province_choices': province_choices,
    'price_choices': price_choices,
    'bedroom_choices': bedroom_choices,
    'listings': queryset_list,
    'values': request.GET
  }
  return render(request, 'listings/search.html', context)
