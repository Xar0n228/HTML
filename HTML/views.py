

from django.shortcuts import render


def product(request):
    return render(request, 'test.html')