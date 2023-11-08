from django.shortcuts import render

# Create your views here.
def star(request):
  return render(request,'star.html')
