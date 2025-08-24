from django.urls import path
from . import views

urlpatterns = [
    # The login page is now the homepage, that Money Morph animation that you started with, can't get it because it stright out leads to the login page to save time, we'll put the money morph at the top
    path('', views.login_view, name='login'),
    
    # We rename 'dashboard' to 'portfolio' to be more descriptive.
    path('portfolio/', views.portfolio_view, name='portfolio'),
    
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
]