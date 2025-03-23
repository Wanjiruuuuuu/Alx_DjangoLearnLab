from django.shortcuts import render, redirect
from django.contrib.auth import login, logout # Handles user login and logouts
from django.contrib.auth.forms import AuthenticationForm  #Built in login forms
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    return render(request, 'blog/profile.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST) # Bind form with user data
        if form.is_valid():  # Validate form fields
            User = form.save() # save user to the database
            login(request, User) #automatically login the user
        return redirect('Profile')  # Display an empty registration form
    
    else:
        
        form = UserRegisterForm() # Create an empty form
    
    return render(request, 'users/register.html', {'form': form}) # Render the registration form with the given template


