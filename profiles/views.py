from django.shortcuts import render, get_object_or_404
from .models import UserProfile
from .forms import UserProfileForm
from django.contrib import messages
from checkout.models import Order
# Create your views here.

def profile(request):
    """ User's profile """
    profile = get_object_or_404(UserProfile, user=request.user)
    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    if request.method == 'POST':
        form = UserProfileForm(request.POST, intance=profile)
        if form .is_valid():
            form.save()
            messages.success(request, 'Profile updated!')

    template = 'profiles/profiles.html'
    context = {
        'form': form,
        'profile': profile,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order=order_number)

    messages.info(request, f'Order History')

    template = 'checkout/checkout_success.html'

    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)