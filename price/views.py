from django.shortcuts import render
from .models import PriceList

# @cache_page(60 * 5)
def price(request):
    services = PriceList.objects.all()
    return render(request, 'barber/price.html', {'services': services})

