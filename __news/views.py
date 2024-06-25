from django.shortcuts import render,redirect
from .models import News
from __main .models import Comments
from __main .form import Newsletter

def News_page(request):
    if request.method== 'GET':    
        form=Newsletter()
        comments=Comments.objects.all()
        news=News.objects.all()
        
        return render(request, 'news.html',{'news':news,'comments':comments, 'form':form})
    
    else:
        form=Newsletter()
        comments=Comments.objects.all()
        return render(request, 'contactus.html', {'comments':comments, 'form':form})    

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