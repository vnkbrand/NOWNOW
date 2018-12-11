from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

from contacts.models import Contact

# Methods for view - linked to urls.py
def register(request):
  if request.method == 'POST':
    # Register User - get form values
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    password2 = request.POST['password2']

    # Check if passwords match
    if password == password2:
      # Check username already exists
      if User.objects.filter(username=username).exists():
        messages.error(request, 'That username is taken.')
        return redirect('register')
      else:
        if User.objects.filter(email=email).exists():
          messages.error(request, 'That email is taken.')
          return redirect('register')
        else:
        # Everything passed - register user
          user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
          # Reg success & redirect to login
          user.save()
          messages.success(request, 'You are now registered.')
          return redirect('login')

    else:
      # If no match
      messages.error(request, 'Passwords do not match.')
      return redirect('register')
  else:
    return render(request, 'accounts/register.html')

def login(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)

    # If user is found in DB
    if user is not None:
      auth.login(request, user)
      messages.success(request, 'You are now logged in.')
      return redirect('dashboard')
    # User not found
    else:
      messages.error(request, 'Invalid credentials.')
      return redirect('login')
  else:
    return render(request, 'accounts/login.html')

def logout(request):
  if request.method == 'POST':
    auth.logout(request)
    messages.success(request, 'You are now logged out.')
    return redirect('index')

def dashboard(request):
  user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)

  context = {
    'contacts': user_contacts
  }
  return render(request, 'accounts/dashboard.html', context)
  