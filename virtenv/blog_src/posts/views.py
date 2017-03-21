from djanjo.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# trydjango1.9 youtube series lesson 10 0f 38
def posts_home(request):
	return HttpResponse("<h1>Hello<h1>")