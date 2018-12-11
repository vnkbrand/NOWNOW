# Home Page View

from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from agents.models import Agent
from listings.choices import price_choices, bedroom_choices, province_choices


def index(request):
  # Show 3 latest listings on the home page
  listings = Listing.objects.order_by('list_date').filter(is_published=True)[:3]

  context = {
    'listings': listings,
    'province_choices': province_choices,
    'price_choices': price_choices,
    'bedroom_choices': bedroom_choices
  }

  return render(request, 'pages/index.html', context)

def about(request):
  # Get all agents
  agents = Agent.objects.order_by('-hire_date')

  # Get MVP
  mvp_agents = Agent.objects.all().filter(is_mvp=True)

  context = {
    'agents': agents,
    'mvp_agents': mvp_agents
  }

  return render(request, 'pages/about.html', context)

