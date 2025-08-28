from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.
def loginview(request):
    if request.method=='POST':
        form=AuthenticationForm(request,request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('dashboard')
    else:
        form=AuthenticationForm()
    return render(request,'login.html',{'form':form})


def dashboard_view(request):
    return render(request,'dashboard.html')