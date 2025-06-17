from django.shortcuts import render

def home(request):
    return render(request, 'deetail/index.html')


def bills(request):
    return render(request, 'bills/bills.html')


def tickets(request):
    return render(request, 'tickets/tickets.html')


def customers(request):
    return render(request, 'customers/customers.html')


def leads(request):
    return render(request, 'leads/leads.html')


def expenses(request):
    return render(request, 'expenses/expenses.html')


def properties(request):
    return render(request, 'properties/properties.html')


def unit_types(request):
    return render(request, 'unit_types/unit_types.html')