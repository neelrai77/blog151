from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from App_Login.forms import SignUpForm
# Create your views here.
def sign_up(request):
    form=SignUpForm()
    registered=False
    if request.method=='POST':
        form =SignUpForm(data=request.POST)
        if form.is_valid():
            form.save()
            registered=True
    
    dict = {'form':form ,'registered':registered}
    return render(request, 'App_Login/signup.html', context =dict)
