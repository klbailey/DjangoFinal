# finalAssessment>myapp>views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, LoginForm, TravelPlanForm
from .models import TripSchedule, TravelPlan
from django.contrib.auth.models import AnonymousUser

def home(request):
    return redirect('dashboard')


def login_registration(request):
    login_form = LoginForm()  # Define login_form outside the if-else blocks
    if request.method == 'POST':
        if 'register' in request.POST:
            register_form = RegistrationForm(request.POST)
            if register_form.is_valid():
                register_form.save()
                # Redirect to the travel dashboard after successful registration
                return redirect('dashboard')
        elif 'login' in request.POST:
            login_form = LoginForm(request.POST)  # Define login_form here as well
            if login_form.is_valid():
                username = login_form.cleaned_data['username']
                password = login_form.cleaned_data['password']
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    # Redirect to the travel dashboard after successful login
                    return redirect('dashboard')
    else:
        register_form = RegistrationForm()
    return render(request, 'login_registration.html', {'register_form': register_form, 'login_form': login_form})

def user_logout(request):
    logout(request)
    return redirect('login')

def dashboard(request):
    # debug
    print(request.user.username) 
    user_name = request.user.username

    trip_schedules = []
    other_travel_plans = []

    if request.user.is_authenticated:
        user_name = request.user.username
        trip_schedules = TripSchedule.objects.filter(user=request.user)
        other_travel_plans = TravelPlan.objects.exclude(tripschedule__user=request.user)
        
    if request.method == 'POST' and 'logout' in request.POST:
        logout(request)
        return redirect('login_registration')

    return render(request, 'dashboard.html', {'user_name': user_name, 'trip_schedules': trip_schedules, 'other_travel_plans': other_travel_plans})
    
@login_required
def add_travel_plan(request):
    if request.method == 'POST':
        form = TravelPlanForm(request.POST)
        if form.is_valid():
            travel_plan = form.save(commit=False)  
            travel_plan.save()  
            # Associate the travel plan with the current user
            trip_schedule = TripSchedule.objects.create(user=request.user, travel_plan=travel_plan)
            return redirect('dashboard')  
    else:
        form = TravelPlanForm()
    return render(request, 'add_travel_plan.html', {'form': form})

def destination(request, travel_plan_id):
    # Retrieve the travel plan using the provided ID
    travel_plan = TravelPlan.objects.get(id=travel_plan_id)
    return render(request, 'destination.html', {'travel_plan': travel_plan})
