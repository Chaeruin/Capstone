from django.urls.conf import path
from user import views

app_name = "user"
urlpatterns = [
        path( "user", views.User.as_view(), name="user" ),
        path("login",views.Login.as_view(), name="login"),
        path("signin",views.Signin.as_view(), name="signin")
    ]