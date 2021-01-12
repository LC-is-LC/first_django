from django.shortcuts import render, redirect
# django has a FORM to create new Users, but also we will further inherit and add extra fields to the form in a new forms.py file
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
# importing flash messages, which is a message that shows one time for a particular activity
# types of messages; debug, success, error, warning, info
# we also add the flash messages to base template so it can pop up to any page
from django.contrib import messages
# Importing a decorator which says that a login is required for the view(function) to be accessed
from django.contrib.auth.decorators import login_required

# Creating the registration GUI for Users

def register(request):
    # we have POST requests and GET requests, this form is a post request to send (post) info somewhere
    if request.method == 'POST':
        # creates form with post data (usually from our form
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}, Login now!')
            return redirect('login')
    else:
        # blank form
        form = UserRegisterForm()
    return render(request, 'Users/register.html', {'form': form})
    # There are many HTMl created forms already

@login_required
def profile(request):
    # we have POST requests and GET requests, this form is a post request to send (post) info somewhere
    if request.method == 'POST':
        # we put the instances as requests so that when the forms come up they have the current values
        # The newly submitted data i.e POST will become the new request i.e new value thus the request.POST
        # For the profile which will submit a new file i.e Image, it becomes the new file, thus the request.FILES
        u_form = UserUpdateForm(request.POST,
                                instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        # If both forms are valid, we save them, send a flash message and redirect back to profile page
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated')
            return redirect('profile')

    # If we are not posting i.e updating info, it should remain the same
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    # Create a context that will also be rendered, and will contain our forms in case we want to update
    context = {
        'u_form' : u_form,
        'p_form' : p_form
    }
    return render(request, 'Users/profile.html', context)
