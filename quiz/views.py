from django.shortcuts import render

def startpage(request):
	return render(request, "start.html")

def quiz(request, quiz_number):
