from django.urls import path
from . import views

urlpatterns=[
    path('',views.transaction_list,name='transaction_list'),
    path('add/',views.add_transaction,name='add_transactions'),
    path('delete/<int:id>/', views.delete_transaction, name='delete_transaction'),
    path('edit/<int:id>/',views.edit_transaction,name="edit_transaction"),
    path('show_all/',views.show_all,name='show_all'),
]