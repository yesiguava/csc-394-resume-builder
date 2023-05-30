from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
import openai, os, json
from dotenv import load_dotenv
from user.models import User
load_dotenv()

#this request displays index page as main page and "home" redirection from nav bar
def index_view(request):
    return render(request, 'index.html')

#this request displays about page as "about" redirection from nav bar
def about_view(request):
    return render(request, 'about.html')

#this request displays about page as "contact" redirection from nav bar
def contact_view(request):
    return render(request, 'contact.html')

#this request displays about page as "signin" redirection from nav bar
def signin_view(request):
    return render(request, 'signin.html')

#this request displays about page as "qualifications" redirection from nav bar
def qualifications_view(request):
    return render(request, 'qualifications.html')

#this request displays about page as "output" redirection after submitting qualifications
def output_view(request):
    print(User.objects.last())
    person = User.objects.last()
    jayson = json.loads(person.resume_info)
    print(jayson['name'])
    context = {'Name': jayson['name'], 'Email': jayson['email'],
               'Phone': jayson['phone'], 'Address' : jayson['address'],
               'Education': jayson['education'], 'Experience': jayson['experience'],
               'Skills': jayson['skills'], 'References': jayson['references'],
               'Objective': jayson['objective'], 'Description': jayson['description']}
    return render(request, 'output.html', context)

#this request will display qualifications and need to figure out routing of response from api to another page
api_key = os.getenv('api_key', None)

#handles chatgpt api call sending in qualifications form as json and retrieving then storing json response into database
def submit_form(request):
    chat_response = None
    if api_key is not None and request.method == 'POST':
        openai.api_key = api_key
        user_input = request.POST.dict()
        user_input.pop('csrfmiddlewaretoken')
        print(request.POST.dict())
        prompt = f"Please generate a resume using the following information and structure it in JSON format: {user_input}"

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            #prompt = prompt,
            #max_tokens=256,
            #stop=".",
            messages = [
            {'role': 'user', 'content': prompt}
            ],
            temperature=1
        )
        print(prompt)
        print(response)

        chat_response = response["choices"][0]["message"]["content"]
    
        if chat_response is not None:
            json_input = User.objects.create(resume_info=chat_response)
            json_input.save()
            print(json_input)
            return redirect('output-name')


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
			return redirect('login')
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request, 'register.html', {"register_form":form})

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
	return render(request, 'login.html', {"login_form":form})