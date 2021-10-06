from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from .forms import signUpForm
# Create your views here.

def signup(request):
    form=signUpForm()
    if request.method =='POST':
        form=signUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            auth_login(request,user)
            return redirect('indrex')
    return render(request,'signup.html',{'form':form})


