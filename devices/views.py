from datetime import date
from decimal import Decimal

from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Sum
from django.db.models.functions import Round
from django.http import QueryDict
from django.shortcuts import render
from .models import *


# Create your views here.
@login_required()
def index(request):
    return render(request, 'index.html')

@login_required()
def devices_page(request):
    today = date.today()
    search_params = {
        'name__icontains': request.GET.get('name__icontains'),
        'subdivision__icontains': request.GET.get('subdivision__icontains'),
        'factory_number__icontains': request.GET.get('factory_number__icontains'),
        'sensor__icontains': request.GET.get('sensor__icontains'),
        'quantity__gte': request.GET.get('quantity__gte'),
        'quantity__lte': request.GET.get('quantity__lte'),
        'date_issued__gte': request.GET.get('date_issued__gte'),
        'date_issued__lte': request.GET.get('date_issued__lte'),
        'date_entry__gte': request.GET.get('date_entry__gte'),
        'date_entry__lte': request.GET.get('date_entry__lte'),
        'date_verification__gte': request.GET.get('date_verification__gte'),
        'date_verification__lte': request.GET.get('date_verification__lte'),
        'date_next_verification__gte': request.GET.get('date_next_verification__gte'),
        'date_next_verification__lte': request.GET.get('date_next_verification__lte'),
        'repair_result__icontains': request.GET.get('repair_result__icontains'),
        'state__icontains': request.GET.get('state__icontains'),
    }
    search_querydict = QueryDict(mutable=True)
    for key, value in search_params.items():
        if value:
            search_querydict[key] = value

    devices = Device.objects.all().order_by('id')
    for field, value in search_params.items():
        if value:
            if field.startswith(('price', 'sum')):
                devices = devices.filter(**{field: float(value.replace(',', '.'))})
            else:
                devices = devices.filter(**{field: value})

    devices_count = len(devices)

    items_per_page = 60

    paginator = Paginator(devices, items_per_page)

    page_number = request.GET.get('page')

    try:
        devices = paginator.page(page_number)
    except PageNotAnInteger:
        devices = paginator.page(1)
    except EmptyPage:
        devices = paginator.page(paginator.num_pages)

    return render(request, 'main_sklad.html', {'devices': devices,
                                               'today': today,
                                               'devices_count': devices_count,
                                               'search_querydict': search_querydict.urlencode(),
                                               })
