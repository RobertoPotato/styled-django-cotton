from django.shortcuts import render

def financial_report(request):
    return render(request, 'reports/financial_report.html')

def occupation_report(request):
    return render(request, 'reports/occupation_report.html')

def property_report(request):
    return render(request, 'reports/property_report.html')
