from django.shortcuts import render
from . models import Post

# Create your views here.
def hi(request):
   
   return render(request,'i.html')
def dislay(request):
    uf=Post.objects.all()
    
    return render(request,'final.html',{'uf': uf})