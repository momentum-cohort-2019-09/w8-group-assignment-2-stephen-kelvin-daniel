from django.shortcuts import render


def dashboard(request):
    return render(request, 'Flash/dashboard.html')


def testing(request):
    return render(request, 'Flash/testing.html')
