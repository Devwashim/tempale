from django.db import IntegrityError
from django.shortcuts import redirect, render
from django.contrib.auth import  login as auth_login
from django.contrib.auth import  logout
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib import messages




def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def gallery(request):
    return render(request, 'gallery.html')

def contact(request):
    return render(request, 'contact.html')

def dashboard(request):
    return render(request, 'dashboard.html')


def newhome(request):
    return render(request, 'newhome.html')

def client(request):
    return render(request, 'client.html')

def tail(request):
    return render(request, 'tail.html')



def Logout(request):
    logout(request)
    return redirect('login')

# login up view functions

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user) # type: ignore
            messages.success(request, 'Login successful!')
            return redirect('dashboard')  # Redirect to home after successful login
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})


# sign up view functions
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            try:
                # Save the user data to the database
                form.save()
                messages.success(request, 'Registration successful!')
                return redirect('login')  # Redirect to login after successful registration
            except IntegrityError as e:
                # Handle any database integrity issues (e.g., duplicate emails)
                messages.error(request, f"Database error: {str(e)}")
        else:
            # Form validation failed
            messages.error(request, 'There was an error with your registration.')
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})


from django import forms



# from .forms import Contact



# def contact(request):
#     if request.method == "POST":
#         search_form = Contact(request.POST, request.FILES)
#         if search_form.is_valid():
#             search_form.save()
#             messages.success(request, 'Your message has been sent successfully!')
#             return redirect('contact')  # Redirect to contact page or another page
#         else:
#             messages.error(request, 'There was an error with your submission.')
#     else:
#         form = Contact() # type: ignore

#     return render(request, 'contact.html', {'form': form, 'show_feedback_button': True})



# def contact(request):
#     if request.method == 'POST':
#         form = Contact(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Your message has been sent successfully!')
#             return redirect('contact')  # Redirect to contact page or another page
#         else:
#             messages.error(request, 'There was an error with your submission.')
#     else:
#         form = Contact() # type: ignore

#     return render(request, 'contact.html', {'form': form, 'show_feedback_button': True})