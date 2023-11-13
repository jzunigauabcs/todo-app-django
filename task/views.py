from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    context = {}
    template = "task/index.html"
    return render(request, template, context)