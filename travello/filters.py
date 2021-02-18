import django_filters
from django_filters import RangeFilter,BooleanFilter,ModelChoiceFilter
from django import forms
from django.utils.translation import ugettext as _
from django.forms.utils import flatatt
from .models import *

class Watch_Perf_Filter(django_filters.FilterSet):
   price = RangeFilter()
   offer = BooleanFilter()
   class Meta:
       model = watches
       model = perfumes

       fields = ['price','offer','brand']

class Cloth_Shoe_Filter(django_filters.FilterSet):
   price = RangeFilter()
   sale = BooleanFilter()
   class Meta:
       model = cloth
       model = shoes

       fields = ['price','sale','brand']


