from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Item,Borrowed_item
from django.contrib.auth.decorators import login_required


@login_required(login_url='user-login')
def index(request):
    item = Item.objects.all()

    context = {
        'item': item,
    }
    return render(request, 'dashboard/index.html', context)


def scan(request):
    return render(request, 'dashboard/scan.html')


def borrowed(request):
    borrowed = Borrowed_item.objects.all()
    user = User.objects.all()

    context = {
        'borrowed': borrowed,
        'user': user,
    }
    return render(request, 'dashboard/borrowed.html', context)

