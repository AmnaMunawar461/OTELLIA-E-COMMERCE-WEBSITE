from django.urls import path
from . import views
urlpatterns = [
    
path('1',views.m_shoes,name='m_shoes'),
path('2',views.f_shoes,name='f_shoes'),
path('3',views.watch,name='watch'),
path('4',views.m_cloths,name='m_cloths'),
path('5',views.f_cloths,name='f_cloths'),
path('6',views.perfume,name='perfume')]