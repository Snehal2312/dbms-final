from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
# Create your views here.
def customer(request):
    if request.method == 'POST':
         first_name = request.POST['first_name']
         last_name = request.POST['last_name']
         email = request.POST['email']
         username = request.POST['username']
         
         user = User.objects.create_user(first_name = first_name,last_name = last_name,email = email,username = username)
         user.save();
         print("user created")
         return redirect('/')


    else:    
           return render(request,'customer.html')