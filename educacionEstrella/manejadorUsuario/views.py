from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .models import Profile
from .forms import UserRegisterForm
from django.core.mail import send_mail  
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin

PRIVATE_IPS_PREFIX = ('10.', '172.', '192.', )


@login_required
def profile(request):
    return render(request, 'profile.html')
 
@login_required
def passwordChange(request):
    username = request.user.username
    email = request.user.email
    htmly = get_template('password_reset_email')
    d = { 'username': username }
    subject, from_email, to = 'Password Change', 'educacionestrellafake@gmail.com', email
    html_content = htmly.render(d)
    msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()

    return render(request, 'index')

def get_client_ip(request):
    remote_address = request.META.get('HTTP_X_FORWARDED_FOR') or request.META.get('REMOTE_ADDR')
    ip = remote_address
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        proxies = x_forwarded_for.split(',')
        while (len(proxies) > 0 and proxies[0].startswith(PRIVATE_IPS_PREFIX)):
            proxies.pop(0)
            if len(proxies) > 0:
                ip = proxies[0]
        return ip
  
#################### index #######################################
def index(request):
    return render(request, 'Index.html', {'title':'index'})
  
########### register here #####################################
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            form.save()
            ######################### mail system ####################################
            htmly = get_template('Email.html')
            d = { 'username': username }
            subject, from_email, to = 'welcome', 'educacionestrellafake@gmail.com', email
            html_content = htmly.render(d)
            msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            ##################################################################
            messages.success(request, f'Your account has been created ! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'Register.html', {'form': form, 'title':'reqister here'})
  
################ login forms###################################################
def Login(request):
    if request.method == 'POST':
        # AuthenticationForm_can_also_be_used__
        username = request.POST['username']
        password = request.POST['password']
        usuario = authenticate(request, username = username, password = password)
        if usuario is not None:
            form = login(request, usuario)
            messages.success(request, f' wecome {username} !!')
            return redirect('index')
        else:
            messages.info(request, f'account done not exit plz sign in')
    form = AuthenticationForm()
    return render(request, 'Login.html', {'form':form, 'title':'log in'})

class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('index')

class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'password_reset.html'
    email_template_name = 'password_reset_email.html'
    success_message = "We have emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you do not receive an email, " \
                      "please make sure you have entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('logout')

    