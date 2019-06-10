from django.http import HttpResponse
from django.shortcuts import render


#Our view pages

def home_page(request):
    return render(request,"home.html")
def about_page(request):
    return render(request,"about.html")
def contact_page(request):
    return render(request,"contact.html")
