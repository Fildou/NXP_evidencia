from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Item, Borrowed_item


@login_required(login_url='user-login')
def index(request):
    item = Item.objects.all()

    context = {
        'item': item,
    }
    return render(request, 'dashboard/index.html', context)


@login_required(login_url='user-login')
def borrowed(request):
    borrowed = Borrowed_item.objects.all()
    user = User.objects.filter(groups=2)
    item = Item.objects.all()

    context = {
        'borrowed': borrowed,
        'user': user,
        'item': item,
    }
    return render(request, 'dashboard/borrowed.html', context)


@login_required(login_url='user-login')
def detail(request, item_PN):
    item = Item.objects.get(item_PN=item_PN)
   # data = request.POST
    #action = data.get('borrow')
    #if request.method == 'POST':
   #     if action == 'borrow':
    return render(request, 'dashboard/detail.html', {'item': item})


@login_required(login_url='user-login')
def scan(request):
    return render(request, 'dashboard/scan.html')


