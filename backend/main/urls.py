from django.urls.conf import path
from main import views
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static

app_name = "main"
urlpatterns = [
        path( "main", views.Main.as_view(), name="main" ), 
        path( "login", views.Login.as_view(), name="login" ) , 
        path( "signup", views.Signup.as_view(), name="signup" ),
        path( "scandata", views.Scandata.as_view(), name="scandata" ),
        path( "totaldata", views.Totaldata.as_view(), name="totaldata" ),    
        path( "averagedata", views.Averagedata.as_view(), name="averagedata" ),  
        path( "perioddata", views.Perioddata.as_view(), name="perioddata" ),  
        path( "alarm", views.Alarm.as_view(), name="alarm" ),  
        path( "logout", views.LogoutView.as_view(), name="logout" ),
        path("idchk", views.IdChkView.as_view(), name="idchk"),
        path("imageupload", views.ImageUploadView.as_view(), name="imageupload"),
    ]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)