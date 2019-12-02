from django.shortcuts import render, HttpResponse

# Create your views here.

def requestreciever(request, *args, **kwargs):
    print(request.GET)
    print(request.POST)
    return HttpResponse(request.GET, request.POST)