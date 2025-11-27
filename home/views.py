from django.shortcuts import render

def home (request):
    if request.method =='POST':
        ...
    else:
        return render(request,'home.html')
