from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.http import HttpResponse, HttpResponseRedirect
from barber.forms import UserRegisterForm, UserLoginForm
from django.core.exceptions import ValidationError
from django.views.generic import ListView, DetailView, CreateView, FormView


def registration(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        print('form-----------------', form)
        if form.is_valid():
            user = form.save()
            print('request-----------------', user)
            print('form.save()-----------------', user)
            login(request, user)
            # messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('index')
        else:
            messages.error(request, 'Ошибка регистрации')
            return render(request, 'barber/registration.html', {"form": form})
    else:
        form = UserRegisterForm()
    return render(request, 'barber/registration.html', {"form": form})


class RegistrationCreateView(CreateView):
    form_class = UserRegisterForm
    template_name = 'barber/registration.html'
    success_url = '/'
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')



def user_logout(request):
    logout(request)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Ошибка авторизации')
    else:
        form = UserLoginForm()
    return render(request, 'barber/login.html', {"login_form": form})
