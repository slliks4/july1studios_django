from django.shortcuts import render,redirect
from .booking_form import Book
from __main .models import Comments
from __main .form import Newsletter

 
def Booking(request):
        if request.method =='GET':
            comments=Comments.objects.all()
            form=Book()
            return render(request, 'booking.html', {'form':form, 'comments':comments})
        else:
            comments=Comments.objects.all()
            form=Book(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                return render(request, 'success.html',{'comments':comments, 'form':form})
            else:
                return redirect('booking')

    
def Base(request):
    form=Newsletter(request.POST,request.FILES)
    if form.is_valid():
        comments=Comments.objects.all()
        form.save()
        return render(request, 'success.html',{'comments':comments, 'form':form})