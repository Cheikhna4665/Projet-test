from django.shortcuts import render,HttpResponseRedirect,redirect 
from django.http import HttpResponse 
from classe.models import classe
from .forms import etudRegistration
from .models import etud
from django.contrib import auth,messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q



# Import pagination
from django.core.paginator import Paginator


# Create your views here.


@login_required

def list(request):
    return render(request,'etudiant/liste_etudiant.html')
@login_required

def home(request):
    stud = etud.objects.all()
    # recherche
    if request.method=='GET':
        name=request.GET.get('q')
        if name:
            stud = etud.objects.filter(name=name)
        
    
    # Pagination
    q = request.GET.get('q', '')  
    print("Search query:", q)
    etuds = etud.objects.filter(
    Q(name=q) | Q(code=q) | Q(prenom=q) | Q(N_Tel=q) | Q(classe=q))

    p = Paginator(etuds, 2)
    page = request.GET.get('page')
    venues = p.get_page(page)

    if request.method == 'POST':
        fm = etudRegistration(request.POST)
        if fm.is_valid():
            cd = fm.cleaned_data['code']
            nm = fm.cleaned_data['name']
            pr = fm.cleaned_data['prenom']
            tl = fm.cleaned_data['N_Tel']
            cls = fm.cleaned_data['classe']
            reg = etud(code=cd, name=nm, prenom=pr, N_Tel=tl, classe=cls)
            reg.save()
            fm = etudRegistration()
        return redirect('accueil')
    else:
        
        fm = etudRegistration()
    
    # Pass queryset of class names to the form
    fm.fields['classe'].queryset = classe.objects.all()
    
    
    return render(request, 'etudiant/acceuil.html', {'form': fm, 'stu': stud, 'venues': venues, 'etuds': etuds})


# cette fonction permer de modifier les information d'un etudient
@login_required
def update_etudient(request , id):
    if request.method=='POST':
        pi = etud.objects.get(pk=id)
        fm = etudRegistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
        return redirect('accueil')
    else:
        pi=etud.objects.get(pk=id)
        fm=etudRegistration(instance=pi)
        
    return render(request,'etudiant/update_etudient.html',{'form':fm})


#cette fonction permer de suprumer le donner
@login_required
def delete_etudient(request,id):
    if request.method=='POST':
        pi=etud.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/home')

#login

def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=auth.authenticate(username=username,password=password)
        if user is not None :
            auth.login(request,user)
            messages.success(request, 'Bienvenu')
            return redirect('/accueil')
        else:
            messages.info(request, 'Invalide login')
    return render(request,'etudiant/login.html')

def logout(request):
    auth.logout(request)
    messages.info(request,'you have been logged out !!')
    return redirect('/')



