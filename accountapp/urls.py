from django.urls import path

from accountapp.views import signup

app_name="accountapp"

urlpatterns=[
    path('signup/',signup,name='signup')
]