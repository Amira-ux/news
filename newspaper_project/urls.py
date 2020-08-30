from django.contrib import admin
from django.urls import path,include



urlpatterns = [
    path('admin/', admin.site.urls),
    path("users/",include("users.urls")),
    path("users/",include("django.contrib.auth.urls")),
    path("articles/",include("articles.urls")),
    path("",include("pages.urls")),
    path("api/v1/",include("api.urls")),
    path("api-auth/",include("rest_framework.urls")),
    path("api/v1/rest-auth/",include("rest_auth.urls")),
   
]
