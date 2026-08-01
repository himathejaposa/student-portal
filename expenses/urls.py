from django.urls import path
from . import views
from . import api_views

urlpatterns = [
    path('', views.expense_list, name='expense_list'),
    path('api/', api_views.expense_api_list, name='expense_api_list'),
]