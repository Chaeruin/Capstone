from django.urls.conf import path
from main import views

app_name = "main"
urlpatterns = [
        path( "main", views.Main.as_view(), name="main" ), 
        path( "login", views.Login.as_view(), name="login" ) , 
        path( "signup", views.Signup.as_view(), name="signup" ),
        path( "scandata", views.Scandata.as_view(), name="scandata" ),
        path( "datainner", views.Datainner.as_view(), name="datainner" ),    
    ]