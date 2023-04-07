from django.urls import path

from .views import index
from price.views import price
from authorization.views import registration, user_login, user_logout, RegistrationCreateView
from shop.views import catalog, ItemDetailView
from django.views.decorators.cache import cache_page

urlpatterns = [
    # path('', cache_page(60*15)(index), name='index'),
    path('', index, name='index'),
    path('catalog', cache_page(60*15)(catalog), name='catalog'),
    path('catalog/<int:pk>/', cache_page(60)(ItemDetailView.as_view()), name='product'),
    path('price', cache_page(60*15)(price), name='price'),
    path('registration', RegistrationCreateView.as_view(), name='registration'),
    path('logout', user_logout, name='logout'),
    path('user_login', user_login, name='user_login'),
]
