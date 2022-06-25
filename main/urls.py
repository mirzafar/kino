from django.urls import path
from .views import *

app_name = "api"

urlpatterns = [
    path('', IndexView.as_view()),
]