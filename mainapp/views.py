from django.shortcuts import render
from .models import product

# Create your views here.
def home(request):
    p_data = product.objects.all()
    return render(request,'index-4.html',{'p_data': p_data})
