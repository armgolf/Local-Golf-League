from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserCreateForm, PNumber
from django.contrib.auth import authenticate, login
from golf.models import Events, Payment, Scores
from mysite import settings
import stripe
stripe.api_key = settings.STRIPE_SECRET_KEY

def landingpage(request):
    scores = Scores.objects.all()
    scores = scores.order_by('-score')
    rollups = Events.objects.all()
    return render(request, 'golf/landingpage.html', {'scores':scores, 'rollups':rollups})

def rollups(request):
    rollups = Events.objects.all()
    return render(request, 'golf/rollups.html', {'rollups':rollups})

def payment(request):
    if request.method == "POST":
        token = request.POST.get("stripeToken")
        charge = stripe.Charge.create(
            amount=3700,
            currency="gbp",
            description="Example charge",
            source=token,
            )
        check = Payment.objects.create(check="Yes", name=(request.POST.get('name')), email=(request.POST.get('email')), phone=(request.POST.get('phone')))
        check.save()
    return render(request, 'golf/payment.html', {})

def customform(request):
    form = PNumber()
    return render(request, 'golf/customform.html', {'form': form})
