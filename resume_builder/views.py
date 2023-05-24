from django.shortcuts import render,redirect
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
