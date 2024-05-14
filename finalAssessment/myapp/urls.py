# finalAssessment>myapp>urls.py
from django.urls import path
from .views import login_registration, user_logout, dashboard, add_travel_plan, destination, home

urlpatterns = [
    path('', login_registration, name='login_registration'),
    path('logout/', user_logout, name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
    path('add-travel-plan/', add_travel_plan, name='add_travel_plan'),
    path('destination/<int:travel_plan_id>/', destination, name='destination'), 
    path('home/', home, name='home'), 
]