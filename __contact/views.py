from django.shortcuts import render,redirect
from .models import Contact
from __main .models import Comments
from __main .form import Newsletter

# Create your views here.
def Contact_us(request):
        forms=Newsletter()
        comments=Comments.objects.all()        
        if request.method=='POST':
            first_name=request.POST['first_name']
            email=request.POST['email']
            message=request.POST['message']
            form=Contact(first_name=first_name, email=email, message=message)
            form.save()
            return render(request, 'success.html',{'comments':comments, 'form':forms})        
        else:
            return render(request, 'contactus.html', {'comments':comments, 'form':forms})

def Base(request):
    form=Newsletter(request.POST,request.FILES)
    if form.is_valid():
        form.save()
        return render(request, 'success.html', {'form':form})
    else:
        return redirect('contact')  