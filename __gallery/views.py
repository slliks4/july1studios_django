from django.shortcuts import render
from .models import Gallery_page 
from .models import Category
from __main .models import Comments
from __main .form import Newsletter

def Gallery(request):
    if request.method== 'GET':
        comments=Comments.objects.all()
        categories=Category.objects.all()
        images=Gallery_page.objects.all()
        form=Newsletter()
        return render(request, 'gallery.html',{'images':images, 'categories':categories,'comments':comments,'form':form})
    
    else:
        form=Newsletter(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'success.html')        

def Gallery_others(request,category):
    if request.method== 'GET':
        form=Newsletter()
        comments=Comments.objects.all()
        categories=Category.objects.all()
        name=Category.objects.get(category_name=category)
        images=name.gallery_page.all()
        return render(request, 'gallery_others.html',{'images':images, 'categories':categories,'comments':comments,'form':form})
    
    else:
        form=Newsletter(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'success.html')        


def Gallery_recent(request):
    if request.method== 'GET':
        form=Newsletter()
        comments=Comments.objects.all()
        categories=Category.objects.all().exclude(category_name='recent')
        name=Category.objects.get(category_name='recent')
        images=name.gallery_page.all()
        return render(request, 'gallery_recent.html',{'images':images,'comments':comments,'form':form,'categories':categories})

    else:
        form=Newsletter(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'success.html')        

