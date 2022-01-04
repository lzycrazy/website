from typing import ContextManager
from django.shortcuts import render
from django.http import HttpResponse
from.models import Blog, Carausel, About, Contact,News,Gallery
from django.contrib import messages



# Create your views here.
def index(request):
   if request.method == "POST":
      email=request.POST['email']
     
      news=News(email=email)

      news.save()
      
   
   temp = Carausel.objects.all()   
   tem = Gallery.objects.all()
   latest = Blog.objects.order_by('-timestamp')[0:4]
   context = {
      'allvideopost':tem, 
      'post':temp,
      'latest':latest

   }


   return render(request, "index.html", context)

  

def about(request):
   temp = About.objects.all()
   context = {
      'postabout':temp
   }
   return render(request, "about.html", context)

# def contact(request):
#    if request.method=='POST':
#       name = request.POST.get('name')
#       email = request.POST.get('email')
#       phonenumber = request.POST.get('phonenumber')
#       content = request.POST.get('content')
#       print(name, email, phonenumber, content)

#       if len(name)<2 or len(email)<5 or len(phonenumber)<10 or len(content)<2:
#          messages.error(request, 'Please fill the form correctly!.')
#       else:   
#          contact = Contact(name='name', email='email', phonenumber ='phonenumber', content='content')
#          contact.save()
#          messages.success(request, 'Form submitted succesfully!.')
#    return render(request, "contact.html")   



def contact(request):
    if request.method == "POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        content =request.POST['content']
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<5:
            messages.error(request, "Please fill the form correctly")
        else:
            contact=Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, "Your message has been successfully sent")
    return render(request, "contact.html")



def blog(request):
   tem = Blog.objects.all()
   context = {
      'allpost':tem
   }
   return render(request,"blog.html" ,context)

def postdef(request, slug):
   Blog.views = Blog.views
   querset = Blog.objects.filter(slug=slug).first()
   context = {
      'querset':querset
     }
   return render(request, "post.html", context)






 