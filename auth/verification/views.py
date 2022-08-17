import uuid
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib import messages
from .forms import RegisterForm, LoginForm
from .verify import SendOTP
from .check_code import CheckOTP


# login page view
def login_page(request):
    form = LoginForm(request.POST or none)
    context = {
        "form":form
    }
    if form.is_valid():
        email = form.cleaned_data.get('email')
        try:
            new = User.objects.get(email=email)
            # If a user exists send an otp first
            SendOTP.send_code(email)
            # redirection to the page to enter the otp
            temp = uuid.uuid4()
            return redirect("/otp/{}/{}".format(new.pk, temp))
        except Exception as e:
            messages.error(request,"Wohohoh No such user")
    return render(request, "auth/login.html")

def generate_otp(request, pk, uuid):
    return render(request, 'otp.html')
