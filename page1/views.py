from django.shortcuts import render

# Create your views here.
def doc (request) :
    return render(request,'doc.html')
def style (request):
    return render (request,'doc.css')
def desk (request):
    return render (request,'doc.js')