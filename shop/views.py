from django.shortcuts import render
# from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from .models import Products, ProductCategory, Producer, ProductImage


def catalog(request):
    if request.method == 'GET':
        '''Получение фильтрации по группе товаров из формы'''
        request_dict = request.GET.dict()
        product_group = []
        if 'product-group' in request_dict:
            product_group = request_dict.pop('product-group')

        filter_list = []
        a = request.GET.dict()
        for i in request_dict:
            filter_list.append(i)

        if product_group:
            if filter_list:
                products = Products.objects.filter(category__slug=product_group, producer__slug__in=filter_list)
            else:
                products = Products.objects.filter(category__slug=product_group)
        else:
            if filter_list:
                products = Products.objects.filter(producer__slug__in=filter_list)
            else:
                products = Products.objects.all()
    else:
        products = Products.objects.all()

    categories = ProductCategory.objects.all()
    producers = Producer.objects.all()

    return render(request, 'barber/catalog.html',
                  {'products': products, 'categories': categories, 'producers': producers})


# def item(request, product_id):
#     product = get_object_or_404(Products, pk=product_id)
#     # main_photo =  ProductImage.objects.filter(product_id=product_id).filter(is_main=True).first()
#     # small_photo =  ProductImage.objects.filter(product_id=product_id).filter(is_main=False)[:3]
#     secondary_photos = ProductImage.objects.filter(product_id=product_id)[:3]
#     category = Products.objects.get(pk=product_id).category
#     return render(request, 'barber/item.html',
#                   {'product': product, 'secondary_photos': secondary_photos, 'category': category})


class ItemDetailView(DetailView):
    model = Products
    template_name = 'barber/item.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product_id = (self.get_object().pk)
        context['secondary_photos'] = ProductImage.objects.filter(product_id=product_id)[:3]
        context['category'] = Products.objects.get(pk=product_id).category
        return context