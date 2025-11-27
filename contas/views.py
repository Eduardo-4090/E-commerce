from django.shortcuts import render

def log_in(request):
    if request.method == "POST":
        ...
    else:
        return render(request , 'log_in.html')

def sign_up(request):
    ...
