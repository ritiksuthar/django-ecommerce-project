from django.shortcuts import render, get_object_or_404, redirect
from .models import Cart
from product.models import Product
from django.contrib.auth.decorators import login_required

#add to cart
@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = Cart.objects.get_or_create(
        user=request.user, 
        product=product
    )
    if not created:
        cart_item.quantity +=1
    cart_item.save()
    return redirect('view_cart')

#remove from cart
@login_required
def remove_from_cart(request, cart_id):
    cart_item = get_object_or_404(Cart, id=cart_id)
    cart_item.delete()
    return redirect('view_cart')

#view cart
@login_required
def  view_cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    print(cart_items)
    total_amount = sum(item.total_price for item in cart_items)
    print(total_amount)
    return render(request, 'view_cart.html', {'cart_items':cart_items, 'total_amount':total_amount})


    
   

