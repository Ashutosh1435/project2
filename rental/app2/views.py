from django.shortcuts import render
from django.http import HttpResponse

def new(request):
    return HttpResponse(' i am app2')

