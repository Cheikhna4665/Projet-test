from django.shortcuts import render,redirect
from django.contrib import auth,messages
from django.contrib.auth.forms import UserCreationForm
from .forms import CreerutilUsateur
from django.contrib.auth.decorators import login_required

# Create your views here.
def inscription(request):
    form=CreerutilUsateur()
    if request.method=='POST':
        form=CreerutilUsateur(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,'Compte cree avec succes pour '+ user)
            return redirect('login')
    context={'form':form}
    return render(request,'compte/inscription.html',context)

def loginPage(request):
    context={}
    return render(request,'compte/loginPage.html',context)
