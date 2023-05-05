from django.urls.conf import path
from main import views

app_name = "main"
urlpatterns = [
        path( "main", views.Main.as_view(), name="main" )  
    ]