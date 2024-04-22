from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from sklad.models import MainSklad


# Create your views here.
@login_required()
def index(request):
    return render(request, 'index.html')

def main_sklad(request):
    main_sklads = MainSklad.objects.all()
    return render(request, 'main_sklad.html', {'main_sklads': main_sklads})
