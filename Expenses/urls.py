from django.urls import path
from . import views

urlpatterns=[
    path('',views.transaction_list,name='transaction_list'),
    path('add/',views.add_transactions,name='add_transactions')
]