from django.shortcuts import render,redirect
from .models import Transaction
# Create your views here.
def transaction_list(request):
    transactions=Transaction.objects.all()
    return render(request,'expenses/transaction_list.html',{'transactions':transactions})

def add_transaction(request):
    return render(request,'expenses/add_transaction.html')