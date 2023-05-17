from django.shortcuts import render
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


#this request will display qualifications and need to figure out routing of response from api to another page
api_key = os.getenv('api_key', None)
def chat(request):
    chat_response = None
    if api_key is not None and request.method == 'POST':
        openai.api_key = api_key
        user_input = request.POST.get('user_input')
        prompt = user_input

        response = openai.Completion.create(
            model="gpt-3.5-turbo",
            prompt = prompt,
            #max_tokens=256,
            #stop=".",
            temperature=0.5
        )
        print(response)
    return render(request, 'qualifications.html', {})

