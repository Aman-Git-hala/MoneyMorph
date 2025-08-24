from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Portfolio
from .forms import PortfolioForm

@login_required
def portfolio_view(request):
    # This is the main view for logged-in users.
    # It finds the user's portfolio or creates a new one if it doesn't exist.
    portfolio, created = Portfolio.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        # If the form is submitted, process the data.
        form = PortfolioForm(request.POST, instance=portfolio)
        if form.is_valid():
            form.save()
            return redirect('portfolio') # Redirect to the same page to show the saved data
    else:
        # If it's a normal visit, show the form with the user's current data.
        form = PortfolioForm(instance=portfolio)

    return render(request, 'account/portfolio.html', {'form': form})

def login_view(request):
    # If user is already logged in, redirect them to their portfolio. So many cases here right? Aryan you must be thinking crazy hard you gayboy
    if request.user.is_authenticated:
        return redirect('portfolio')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('portfolio')
    else:
        form = AuthenticationForm()
    
    return render(request, 'account/login.html', {'form': form})

def signup_view(request):
    # you logged in already boy, redirect them to their portfolio.
    if request.user.is_authenticated:
        return redirect('portfolio')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('portfolio')
    else:
        form = UserCreationForm()
    
    return render(request, 'account/signup.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
    return redirect('login') # After logout, send them back to where they came from, idiots