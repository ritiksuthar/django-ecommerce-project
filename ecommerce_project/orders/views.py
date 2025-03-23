from django.shortcuts import render, redirect, get_object_or_404
from .models import Order
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
import razorpay
from product.models import Product
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse

# Razorpay client initialization with API keys from settings
razorpay_client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
   
    return render(request, 'order_history.html', {'orders': orders})


@login_required
def track_order(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    for item in order.cart.all():
        print(item.product_name)
    return render(request, 'track_order.html', {'orders': order})


@login_required
def payment(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    amount = int(product.price * 100)  # Amount in paise for Razorpay

    # Razorpay order creation
    razorpay_order = razorpay_client.order.create({
        "amount": amount,
        "currency": "INR",
        "payment_capture": "1",
    })

    # Save order details in database
    order = Order.objects.create(
        user=request.user,
        total_amount=amount / 100,  # Save amount in rupees
        payment_id=razorpay_order["id"],
    )
    order.save()

    # Send data to template for payment page
    context = {
        "product": product,
        "amount": amount / 100,  # Amount in rupees for display
        "order_id": razorpay_order["id"],
        "razorpay_key": settings.RAZORPAY_KEY_ID,
    }
    return render(request, "payment.html", context)



@csrf_exempt
def payment_success(request):
    if request.method == 'POST':
        # Extract payment details from Razorpay's POST response
        razorpay_order_id = request.POST.get('razorpay_order_id')
        razorpay_payment_id = request.POST.get('razorpay_payment_id')
        razorpay_signature = request.POST.get('razorpay_signature')

        # Verify payment using Razorpay's signature verification (Optional but recommended)
        params_dict = {
            'razorpay_order_id': razorpay_order_id,
            'razorpay_payment_id': razorpay_payment_id,
            'razorpay_signature': razorpay_signature,
        }

        try:
            # Razorpay Signature Verification
            razorpay_client.utility.verify_payment_signature(params_dict)
            # Update order status after successful payment
            order = get_object_or_404(Order, payment_id=razorpay_order_id)
            order.order_status = 'Confirmed'
            order.save()
            return render(request, "success.html", {'payment_id': razorpay_payment_id})
        except razorpay.errors.SignatureVerificationError:
            return HttpResponse("Payment verification failed. Please try again.", status=400)

    return JsonResponse({"error": "Invalid request method."}, status=400)
