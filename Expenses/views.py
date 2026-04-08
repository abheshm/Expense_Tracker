from django.shortcuts import render,redirect
from .models import Transaction
# Create your views here.
def transaction_list(request):
    transactions=Transaction.objects.all().order_by('-date')

    total_income = 0
    total_expense = 0

    for t in transactions:
        if t.type =='income':
            total_income += t.amount
        else:
            total_expense += t.amount

    balance = total_income - total_expense 

    context = {
        'transactions' : transactions,
        'total_income' : total_income,
        'total_expense' : total_expense,
        'balance' : balance
    }
    return render(request,'expenses/transaction_list2.html',context)

def add_transaction(request):
    if request.method=="POST":
        amount = request.POST['amount']
        type = request.POST['type']
        description = request.POST['description']
        date = request.POST['date']

        Transaction.objects.create(amount=amount,type=type,description=description,date=date)

        return redirect('/')
    return render(request,'expenses/add_transaction1.html')

def delete_transaction(request,id):
    transaction = Transaction.objects.get(id=id)

    if request.method=="POST":
        transaction.delete()
        return redirect('/')
    return render(request,'expenses/delete_transaction.html',{'transaction':transaction})

def edit_transaction(request,id):

    transaction = Transaction.objects.get(id=id)

    if request.method=="POST":
        transaction.amount = request.POST['amount']
        transaction.type = request.POST['type']
        transaction.description = request.POST['description']
        transaction.date = request.POST['date']

        transaction.save()

        return redirect('/')
    
    return render(request,'expenses/edit_transaction.html', {"transaction":transaction})

def show_all(request):
    transactions = Transaction.objects.all().order_by('-date')

    context = {
        'transactions': transactions,
    }
    
    return render(request, 'expenses/show_all1.html', context)