from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .models import Order
from produit.models import Produit
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.contrib import messages



def vieworder(request):     
    uid=request.user
    orders= Order.objects.filter(user=uid) 
    return render(request,'produit/vieworder.html',{"orders":orders})