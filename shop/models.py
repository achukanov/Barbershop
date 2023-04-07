from django.db import models


class Products(models.Model):
    product_name = models.CharField(max_length=150, verbose_name='Наименование')
    content = models.TextField(blank=True, verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    category = models.ForeignKey('ProductCategory', on_delete=models.PROTECT, null=True, verbose_name='Категория')
    producer = models.ForeignKey('Producer', on_delete=models.PROTECT, null=True, verbose_name='Производитель')
    on_sale = models.BooleanField(default=True, verbose_name='В продаже')
    units_price = models.IntegerField(verbose_name='Цена')
    units_in_stock = models.IntegerField(verbose_name='Остаток')
    article = models.CharField(max_length=20, verbose_name='Артикул', null=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Главное фото', blank=True)

    def get_absolute_url(self):

        '''return для функции'''
        # return reverse('product', kwargs={"product_id": self.pk})

        '''return для класса RegistrationCreateView'''
        return reverse('product', kwargs={"pk": self.pk})

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['created_at']


class ProductCategory(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Категория')
    slug = models.SlugField(max_length=70, unique=True, verbose_name='SLUG категории')

    def get_absolute_url(self):
        return reverse('category', kwargs={"category_id": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория товаров'
        verbose_name_plural = 'Категории товаров'
        ordering = ['id']


class Producer(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Производитель')
    slug = models.SlugField(max_length=70, unique=True, verbose_name='SLUG производителя')


    def get_absolute_url(self):
        return reverse('category', kwargs={"category_id": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'
        ordering = ['id']


class ProductImage(models.Model):
    product_id = models.ForeignKey('Products', on_delete=models.PROTECT, null=True, verbose_name='Продукт')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Вторичное фото', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def get_absolute_url(self):
        return reverse('image', kwargs={"image_id": self.pk})

    class Meta:
        verbose_name = 'Вторичное фото товара'
        verbose_name_plural = 'Вторичные фото товара'
        ordering = ['product_id', 'id']
