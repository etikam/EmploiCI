from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# from account.views import signin
# Create your views here.


# login_required(login_url=signin)
def home(request):
    
    return render(request,'home.html')
