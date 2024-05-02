from datetime import date
from decimal import Decimal

from django.contrib.auth.decorators import login_required
from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage
from django.db.models import Sum
from django.db.models.functions import Round
from django.http import QueryDict
from django.shortcuts import render

from sklad.models import MainSklad


# Create your views here.
@login_required()
def index(request):
    return render(request, 'index.html')


def main_sklad(request):
    today = date.today()
    search_params = {
        'item_number__icontains': request.GET.get('item_number__icontains'),
        'name__icontains': request.GET.get('name__icontains'),
        'price__gte': request.GET.get('price__gte'),
        'price__lte': request.GET.get('price__lte'),
        'sum__gte': request.GET.get('sum__gte'),
        'sum__lte': request.GET.get('sum__lte'),
        'date_receipt__gte': request.GET.get('date_receipt__gte'),
        'date_receipt__lte': request.GET.get('date_receipt__lte'),
        'number_sklad__icontains': request.GET.get('number_sklad__icontains'),
        'responsible__icontains': request.GET.get('responsible__icontains'),
        'contractor__icontains': request.GET.get('contractor__icontains'),
    }
    search_querydict = QueryDict(mutable=True)
    for key, value in search_params.items():
        if value:
            search_querydict[key] = value

    main_sklads = MainSklad.objects.all().order_by('id')
    for field, value in search_params.items():
        if value:
            if field.startswith(('price', 'sum')):
                main_sklads = main_sklads.filter(**{field: float(value.replace(',', '.'))})
            else:
                main_sklads = main_sklads.filter(**{field: value})

    for main_sklad in main_sklads:
        if main_sklad.price is not None:
            main_sklad.price = Decimal(main_sklad.price).quantize(Decimal('0.01'))
        if main_sklad.quantity is not None:
            main_sklad.quantity = Decimal(main_sklad.quantity).quantize(Decimal('0.01'))
        if main_sklad.sum is not None:
            main_sklad.sum = Decimal(main_sklad.sum).quantize(Decimal('0.01'))
    main_sklads_count = len(main_sklads)
    main_sklads_sum = main_sklads.aggregate(sum=Round(Sum('sum')))

    items_per_page = 60

    paginator = Paginator(main_sklads, items_per_page)

    page_number = request.GET.get('page')

    try:
        main_sklads = paginator.page(page_number)
    except PageNotAnInteger:
        main_sklads = paginator.page(1)
    except EmptyPage:
        main_sklads = paginator.page(paginator.num_pages)

    return render(request, 'main_sklad.html', {'main_sklads': main_sklads,
                                               'today': today,
                                               'main_sklads_count': main_sklads_count,
                                               'main_sklads_sum': main_sklads_sum,
                                               'search_querydict': search_querydict.urlencode(),
                                               })
