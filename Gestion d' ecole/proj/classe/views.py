from django.shortcuts import render,HttpResponseRedirect,redirect
from django.http import HttpResponse
from .forms import classeregistration
from .models import classe
from django.contrib.auth.decorators import login_required
from django.db.models import Q
# Import pagination
from django.core.paginator import Paginator

# Create your views here.

# cette fonction permet d'ajouter et d'afficher les infourmation  des etudient
@login_required
def liste_classe(request):
    clas=classe.objects.all()
    # recherche
    if request.method=='GET':
        name=request.GET.get('q')
        if name:
            clas = classe.objects.filter(name=name)
        
    
    # Pagination
    q = request.GET.get('q', '')  
    print("Search query:", q)
    ets = classe.objects.filter(
    Q(name=q))

    p = Paginator(ets, 2)
    page = request.GET.get('page')
    venues = p.get_page(page)
    if request.method=='POST':
        fmm=classeregistration(request.POST)
        if fmm.is_valid():
            nmm=fmm.cleaned_data['name']
            reg=classe(name=nmm)
            reg.save()
            fmm=classeregistration()
    else:
        fmm=classeregistration()
    # Pass queryset of class names to the form

    
    return render(request,'classe/liste_classe.html',{'form':fmm,'cls':clas,'ets': ets})

# cette fonction permer de modifier les information d'un classe
@login_required
def update_classe(request , id):
    if request.method=='POST':
        pi = classe.objects.get(pk=id)
        fm = classeregistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
        return redirect('classe')
    else:
        pi=classe.objects.get(pk=id)
        fm=classeregistration(instance=pi)

    return render(request,'classe/update_classe.html',{'form':fm})


#cette fonction permer de suprumer le donner
@login_required
def delete_classe(request,id):
    if request.method=='POST':
        pi=classe.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/classe')

    
    

