from django.shortcuts import render
from .models import Images
# Create your views here.

def home(request):
    blo = Images.objects.all().order_by("?")
    return render(request,'index.html', context={'blo':blo})

