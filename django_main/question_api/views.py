from django.shortcuts import render, HttpResponse
import requests

def func(request):
    response = requests.get('https://opentdb.com/api.php?amount=10').json()
    return render(request, 'print.html', response)