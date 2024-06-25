from django.shortcuts import render,redirect
from .form import Newsletter
from __news .models import News
from .models import Gallery_slide,Event_slide,First_slide,Our_service,Comments

def Home(request):
    if request.method=='GET':
        form=Newsletter()
        first_slides=First_slide.objects.all()
        gallery_slides=Gallery_slide.objects.all()
        event_slides=Event_slide.objects.all()
        comments=Comments.objects.all()
        our_services=Our_service.objects.all()
        news=News.objects.all()[:3]
        return render(request, 'index.html',{'news':news,'first_slides':first_slides,'gallery_slides':gallery_slides, 'event_slides':event_slides, 'comments':comments,'our_services':our_services,'form':form})
    else:
        form=Newsletter(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'success.html')
        else:
            return render(request, 'index.html')

def News_readmore(request, slug):
    if request.method== 'GET':    
        form=Newsletter()
        comments=Comments.objects.all()
        news=News.objects.get(slug=slug)
        return render(request, 'news_readmore.html', {'news':news,'comments':comments, 'form':form})
    
    else:
        form=Newsletter()
        comments=Comments.objects.all()
        return render(request, 'contactus.html', {'comments':comments, 'form':form})
    
def About(request):
    if request.method=='GET':
        form=Newsletter()
        comments=Comments.objects.all()
        return render(request, 'about.html',{'comments':comments,'form':form})
    else:
        form=Newsletter(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'success.html')

def Services(request):
    if request.method=='GET':
        form=Newsletter()
        comments=Comments.objects.all()
        return render(request, 'services.html',{'comments':comments,'form':form})
    else:
        form=Newsletter(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'success.html')

def How_we_work(request):
    if request.method=='GET':
        form=Newsletter()
        comments=Comments.objects.all()
        return render(request, 'how_we_work.html',{'comments':comments,'form':form})
    else:
        form=Newsletter(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'success.html')

def Why_us(request):
    if request.method=='GET':
        form=Newsletter()
        comments=Comments.objects.all()
        return render(request, 'why_us.html',{'comments':comments,'form':form})
    else:
        form=Newsletter(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'success.html')

