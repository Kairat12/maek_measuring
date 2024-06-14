from datetime import date
from decimal import Decimal

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Sum
from django.db.models.functions import Round
from django.http import QueryDict
from django.shortcuts import render

from contract_status.models import ContractStatus


# Create your views here.
def contract_status(request):
    today = date.today()
    search_params = {
        'short_description__icontains': request.GET.get('short_description__icontains'),
        'contractor__icontains': request.GET.get('contractor__icontains'),
        'contract_name__icontains': request.GET.get('contract_name__icontains'),
        'contract_sum__gte': request.GET.get('contract_sum__gte'),
        'contract_sum__lte': request.GET.get('contract_sum__lte'),
        'date_receipt__gte': request.GET.get('date_receipt__gte'),
        'date_receipt__lte': request.GET.get('date_receipt__lte'),
        'delivery_deadline__gte': request.GET.get('delivery_deadline__gte'),
        'delivery_deadline__lte': request.GET.get('delivery_deadline__lte'),
        'payment_indicator__icontains': request.GET.get('payment_indicator__icontains'),
        'supervising_service__icontains': request.GET.get('supervising_service__icontains'),
        'responsible__icontains': request.GET.get('responsible__icontains'),
        'contract_status__icontains': request.GET.get('contract_status__icontains'),
        'receipt_warehouse__icontains': request.GET.get('receipt_warehouse__icontains'),
        'responsible_warehouse__icontains': request.GET.get('responsible_warehouse__icontains'),
    }
    search_querydict = QueryDict(mutable=True)
    for key, value in search_params.items():
        if value:
            search_querydict[key] = value

    main_sklads = ContractStatus.objects.all().order_by('id')
    for field, value in search_params.items():
        if value:
            if field.startswith(('price', 'contract_sum')):
                main_sklads = main_sklads.filter(**{field: float(value.replace(',', '.'))})
            else:
                main_sklads = main_sklads.filter(**{field: value})

    for main_sklad in main_sklads:
        if main_sklad.contract_sum is not None:
            main_sklad.contract_sum = Decimal(main_sklad.contract_sum).quantize(Decimal('0.01'))
    main_sklads_count = len(main_sklads)
    main_sklads_sum = main_sklads.aggregate(contract_sum=Round(Sum('contract_sum')))

    items_per_page = 60

    paginator = Paginator(main_sklads, items_per_page)

    page_number = request.GET.get('page')

    try:
        main_sklads = paginator.page(page_number)
    except PageNotAnInteger:
        main_sklads = paginator.page(1)
    except EmptyPage:
        main_sklads = paginator.page(paginator.num_pages)

    return render(request, 'contract_status.html', {'main_sklads': main_sklads,
                                               'today': today,
                                               'main_sklads_count': main_sklads_count,
                                               'main_sklads_sum': main_sklads_sum,
                                               'search_querydict': search_querydict.urlencode(),
                                               })