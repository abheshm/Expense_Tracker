from django.shortcuts import render,redirect
from .models import Transaction
# Create your views here.
def transaction_list(request):
    transactions=Transaction.objects.all().order_by('-date')
    return render(request,'expenses/transaction_list.html',{'transactions':transactions})

def add_transaction(request):
    if request.method=="POST":
        amount = request.POST['amount']
        type = request.POST['type']
        description = request.POST['description']
        date = request.POST['date']

        Transaction.objects.create(amount=amount,type=type,description=description,date=date)

        return redirect('/')
    return render(request,'expenses/add_transaction.html')

def delete_transaction(request,id):
    transaction = Transaction.objects.get(id=id)

    if request.method=="POST":
        transaction.delete()
        return redirect('/')
    return render(request,'expenses/delete_transaction.html',{'transaction':transaction})