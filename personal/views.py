from django.shortcuts import render
from personal.models import Question

# Create your views here.

def home_screen_view(request):
	
	context = {}
	


	# list_of_values = []
	# list_of_values.append('first entry')
	# list_of_values.append('second entry')
	# list_of_values.append('third entry')
	# list_of_values.append('fourth entry')
	# context['list_of_values'] = list_of_values


	questions = Question.objects.all()
	context['questions'] = questions



	return render(request,"personal/home.html",{})


def about(request):
	return render(request, "about.html", {})

def projects(request):
	return render(request, "projects.html", {})

def contacts(request):

	# if request.method == "POST":
	# 	message_name = request.POST['message-name']
	# 	message_email = request.POST['message-email']
	# 	message = request.POST['message']

	# 	return render(request,"contacts.html", {'message_name' : message_name})


	# else:
	# 	return render(request,"contacts.html", {})
	return render(request,"contacts.html", {})




	
