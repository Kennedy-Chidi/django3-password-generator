from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.


def home(request):
	return render(request, 'generator/home.html')

def about(request):
	return render(request, 'generator/about.html')

def password(request):

	characters = list('abcdefghijklmnopuvwxyz')
	thepassword = ''

	if request.GET.get('uppercase'):
		characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

	if request.GET.get('special'):
		characters.extend(list('!@#$%^&*()_+-'))

	if request.GET.get('numbers'):
		characters.extend(list('1234567890'))


	length = int(request.GET.get('len'))
	# length = 10
	for x in range(length):
		thepassword += random.choice(characters)
	return render(request, 'generator/password.html', {'password': thepassword})