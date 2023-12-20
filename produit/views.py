from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Produit
from order.models import Order
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from category.models import Category
from django.contrib import messages
# Create your views here.

@login_required
def produit(request, id):    
    produit= Produit.objects.get(id=id)
    return render(request,'produit/produit.html',{"produit":produit})

@login_required
def invoice(request):    
   uid=request.user
   orderid=0   
   total=0
   orders= Order.objects.filter(user=uid)   
   for order in orders.order_by('id'):       
       orderid=order.id+2024
       orderid=str(orderid).encode("utf-8").hex()
   for order in orders:       
       total+= order.qte*order.product.price
   return render(request,'produit/invoice.html',{"orders":orders,"total":total,"oid":orderid})

@login_required
def liste_produits(request, id): 
    category= Category.objects.get(id=id)
    products = category.cproducts.all()     
    sort_by = request.GET.get('sort_by', 'id')  
    products= products.order_by(sort_by)    
    return render(request,'produit/liste_produits.html',{"products":products,"category":category, 'sort_by': sort_by})


@csrf_exempt 
@login_required  
def create_order(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        product = get_object_or_404(Produit, id=product_id)
        quantity = int(request.POST.get('quantity'))

        if quantity > product.quantity:
            messages.warning(request, 'Error! Order quantity exceeds product quantity')
            return redirect('produit', product_id)

        # Try to get an existing order for the user and product
        order = Order.objects.filter(user=request.user, product=product).first()

        if order:
            # If the order exists, update the quantity
            order.qte += quantity
            order.save()
        else:
            # If the order doesn't exist, create a new one
            order = Order.objects.create(
                qte=quantity,
                user=request.user,
                product=product
            )

        # Update the product stock
        product.quantity -= quantity
        product.save()

        messages.success(request, 'Order completed successfully.')

        return redirect('produit', product_id)

    return redirect('produit')