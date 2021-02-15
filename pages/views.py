from django.shortcuts import render
from django.http import HttpResponse
from properties.choices import price_choices, bedroom_choices, state_choices

from properties.models import Properties
from realtors.models import Realtor


def display_page(request):
    # Get Latest Properties
    latest_properties = Properties.objects.order_by('-list_date').filter(is_published=True)[:5]

    # Get Popular Properties
    popular_properties = Properties.objects.order_by('-city').filter(is_published=True)[:5]

    content = {
        'latest_properties': latest_properties,
        'popular_properties': popular_properties,
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
        'state_choices': state_choices
    }
    return render(request, 'pages/display.html', content)


def about(request):
    # Get all Realtors
    realtors = Realtor.objects.order_by('-hire_date')

    # Get MVP_Realtor
    mvp_realtor = Realtor.objects.all().filter(is_mvp=True)
    content = {
        'realtors': realtors,
        'mvp_realtor': mvp_realtor
    }
    return render(request, 'pages/about.html', content)


def properties(request):
    return render(request, 'pages/properties.html')
