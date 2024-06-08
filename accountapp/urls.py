from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path

from accountapp.views import signup, login_view, logout_view

app_name="accountapp"

urlpatterns=[
    path('signup/',signup,name='signup'),
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
]