from django.shortcuts import render, redirect

# import models
from .models import Decade, Fad

# Create your views here.
def decade_list(request):
  decades = Decade.objects.all()
  return render(request, 
    'nostaldja/decade_list.html', 
    {'decades': decades}
  )

def decade_detail(request, pk):
  decade = Decade.objects.get(id=pk)
  return render(request, 
    'nostaldja/decade_detail.html',
    {'decade': decade}
  )


def fad_list(request):
  fads = Fad.objects.all()
  return render(request, 
    'nostaldja/fad_list.html', 
    {'fads': fads}
  )

def fad_detail(request, pk):
  fad = Fad.objects.get(id=pk)
  return render(request, 
    'nostaldja/fad_detail.html',
    {'fad': fad}
  )
