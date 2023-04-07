# import django_filters
#
#
# from .models import MyModel
#
#
# class MyFilter(django_filters.FilterSet):
#     def __init__(self, *args, **kwargs):
#         super(MyFilter, self).__init__(*args, **kwargs)
#         self.fields['email'].label = "New Email Label"
#     class Meta:
#         model = MyModel
#         fields = {'name': ['exact', 'icontains'],
#                   'price': ['exact', 'gte', 'lte'],
#                  }