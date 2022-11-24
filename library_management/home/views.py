from django.shortcuts import render
from .models import *
# Create your views here.

def home(request):
    ibook=BookIssue.objects.all().order_by('return_date')
    icount=ibook.count()
    context={'icount':icount, 'ibook':ibook}
    return render(request, 'home/home.html', context)

def books(request):
    ibook=Book.objects.all()
    context = {'ibook':ibook}
    return render(request, 'home/books.html', context)

def readers(request):
    ibook=User.objects.all()
    context = {'ibook':ibook}
    return render(request, 'home/readers.html', context)