from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    # path('welcome/', views.welcome_view, name='welcome'),
    path('logout/', views.logout_view, name='logout'),
    path('delete_account/', views.delete_account_view, name='delete_account'),
]
