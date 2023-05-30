from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
import openai, os
from dotenv import load_dotenv
load_dotenv()

#this request displays index page as main page and "home" redirection from nav bar
def index(request):
    return render(request, 'index.html', {})

#this request displays about page as "about" redirection from nav bar
def about(request):
    return render(request, 'about.html', {})


def contact(request):
    return render(request, 'contact.html', {})


def signin(request):
    return render(request, 'signin.html', {})

def qualifications(request):
    return render(request, 'qualifications.html', {})

def output_view(request, message):
    print(message)
    return render(request, 'output.html', {})

#this request will display qualifications and need to figure out routing of response from api to another page
api_key = os.getenv('api_key', None)

def submit_form(request):
    chat_response = None
    if api_key is not None and request.method == 'POST':
        openai.api_key = api_key
        user_input = request.POST.get('user_input')
        prompt = f"Please generate a resume using the following information: {user_input}"

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            #prompt = prompt,
            #max_tokens=256,
            #stop=".",
            messages = [
            {'role': 'user', 'content': prompt}
            ],
            temperature=0.5
        )
        print(response)

        chat_response = response["choices"][0]["message"]["content"]
    
        if chat_response is not None:
            context={'chat_response': chat_response}
            print(prompt)
            return render(request,'output.html', context)


    print(request.POST)
    return render(request, 'qualifications.html', {})

# This is for registering a new user
def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("main:homepage")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="main/register.html", context={"register_form":form})

# This is allows a user to login
def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("main:homepage")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="main/login.html", context={"login_form":form})
