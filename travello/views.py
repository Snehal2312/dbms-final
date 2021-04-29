from django.shortcuts import render
from .models import Fooditem
# Create your views here.
def index (request):
    foodits = Fooditem.objects.all()
    
    return render(request, 'index.html',{'foodits': foodits})
  