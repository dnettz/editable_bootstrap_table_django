from django.urls import path

from . import views

app_name = 'main_app'

urlpatterns = [
    path('', views.index, name='home'),
    path('customer/<str:uid>', views.open_customer, name='open_customer'),
    path('customer/add-record/<str:uid>', views.add_record, name='add_record')
]