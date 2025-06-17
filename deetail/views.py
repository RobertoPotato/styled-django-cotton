from django.shortcuts import render

def home(request):
    return render(request, 'deetail/index.html')


def bills(request):
    return render(request, 'bills/bills.html')


def tickets(request):
    return render(request, 'tickets/tickets.html')


def customers(request):
    return render(request, 'customers/customers.html')
