from django.shortcuts import render


# Create your views here.
def Admin(request):
    return render(request, 'Admin.html')
