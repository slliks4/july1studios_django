from django.shortcuts import render,redirect
from .forms import Apply
from .models import Vacancy,Jobs_available,Application
from __main .models import Comments
from __main .form import Newsletter

def Application(request):
    if request.method=='GET':
        comments=Comments.objects.all()
        form=Apply()
        return render(request, 'apply.html',{'form':form, 'comments':comments})
    
    else:
        forms=Newsletter()
        comments=Comments.objects.all()
        form=Apply(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'success.html',{'comments':comments, 'form':forms})
        else:
            return redirect('application')  

def Base(request):
    form=Newsletter(request.POST,request.FILES)
    if form.is_valid():
        form.save()
        return render(request, 'success.html')
    else:
        return redirect('application')      

def Career_opportunity(request):
    if request.method=='GET':
        comments=Comments.objects.all()
        form=Newsletter()
        careers=Vacancy.objects.all()
        return render(request, 'career.html',{'careers':careers,'comments':comments,'form':form})
    
    else:
        form=Newsletter(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'success.html')
        else:
            return redirect('career')
        