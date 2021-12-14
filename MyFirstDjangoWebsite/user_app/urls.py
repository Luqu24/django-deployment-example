from django.urls import path
from . import views

app_name = 'user_app'

urlpatterns= [
    path("userindex",views.userindex,name="userindex"),
    path("register/",views.register,name="register"),
    path("logout/",views.user_logout,name="logout"),
    path("special/",views.special,name="special"),
    path("login/",views.user_login,name="login")
]
