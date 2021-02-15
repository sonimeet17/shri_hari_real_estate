from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import price_choices, bedroom_choices, state_choices
from django.db.models import Count


from .models import Properties


def display_page(request):
    properties = Properties.objects.order_by('-list_date').filter(is_published=True)

    total_property_count = Properties.objects.filter(is_published=True).count()  # This is used for count total number of count

    paginator = Paginator(properties, 9)
    page = request.GET.get('page')
    paged_properties = paginator.get_page(page)

    context = {
        'properties': paged_properties,
        'total_property_count': total_property_count
    }

    return render(request, 'properties/properties.html', context)


def property(request, property_id):
    property = get_object_or_404(Properties, pk=property_id)

    context = {
        'properties': property
    }

    return render(request, 'properties/property_details.html', context)


def search(request):
    queryset_list = Properties.objects.order_by('-list_date')

    # Keywords
    if 'property_type' in request.GET:
        property_type = request.GET['property_type']
        if property_type:
            queryset_list = queryset_list.filter(description__icontains=property_type)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)

    if 'bedroom' in request.GET:
        bedroom = request.GET['bedroom']
        if bedroom:
            queryset_list = queryset_list.filter(bedrooms__lte=bedroom)

    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)

    if 'max_price' in request.GET:
        max_price = request.GET['max_price']
        if max_price:
            queryset_list = queryset_list.filter(price__gte=max_price)

    context = {
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
        'state_choices': state_choices,
        'properties': queryset_list,
        'values': request.GET
    }
    return render(request, 'properties/search.html', context)
