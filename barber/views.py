from django.shortcuts import render, redirect
from .models import News
from .forms import BookingForm
from telebot.send_message import sendTelegram
from django.views.decorators.cache import cache_page


# @cache_page(60 * 5)
def index(request):
    news = News.objects.all()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            dict_tg = request.POST.dict()
            i = form.save()
            sendTelegram(dict_tg=dict_tg)
            return redirect('index')
    else:
        form = BookingForm()
    return render(request, 'barber/index.html', {'form': form, 'news': news})
