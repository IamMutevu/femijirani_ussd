from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	return render(request, 'web/home.html')

def donate(request):
	return render(request, 'web/donate.html')