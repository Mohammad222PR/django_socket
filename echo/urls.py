from django.urls import path
from .views import *

app_name = 'echo'

# urls
urlpatterns = [
    path('', Index.as_view(), name='index'),
]
