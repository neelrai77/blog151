from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm,PasswordChangeForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

from django.contrib.auth.decorators import login_required
from App_Login.forms import SignUpForm,ProfilePic

# Create your views here.

def sign_up(request):
    form = SignUpForm()
    # registered = False
    if request.method == 'POST':
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            # user.is_active=False
            form.save()
            # registered = True

            template=render_to_string('App_Login/email_template.html', {'name': form.cleaned_data.get('username')})
            email = EmailMessage(
                template,
                settings.EMAIL_HOST_USER,
                [form.cleaned_data.get('email')],
                
            )

    dict = {'form':form, 'registered':registered }
    return render(request, 'App_Login/signup.html',context=dict)

# def login_page(request):
#     form = AuthenticationForm()
#     if request.method == 'POST':
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request,user)
#                 return HttpResponseRedirect(reverse('index'))

#     return render(request,'App_Login/login.html', context={'form':form})

# @login_required
# def logout_user(request):
#     logout(request)
#     return HttpResponseRedirect(reverse('login'))


@login_required
def profile(request):
    return render(request,'App_Login/profile.html', context={})

@login_required
def pass_change(request):
    current_user = request.user
    changed = False
    form = PasswordChangeForm(current_user)
    if request.method == 'POST':
        form = PasswordChangeForm(current_user, data=request.POST)
        if form.is_valid():
            form.save()
            changed = True
    return render(request,'App_Login/pass_change.html', context={'form':form,'changed':changed})

@login_required
def add_pro_pic(request):
    form = ProfilePic()
    if request.method == 'POST':
        form = ProfilePic(request.POST, request.FILES)
        if form.is_valid():
            user_obj = form.save(commit=False)
            user_obj.user = request.user
            user_obj.save()
            return HttpResponseRedirect(reverse('App_Login:profile'))
    return render(request,'App_Login/pro_pic_add.html', context={'form':form})

@login_required
def change_pro_pic(request):
    form = ProfilePic(instance=request.user.user_profile)
    if request.method == 'POST':
        form = ProfilePic(request.POST, request.FILES, instance=request.user.user_profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('App_Login:profile'))
    return render(request,'App_Login/pro_pic_add.html', context={'form':form})
