from django.urls import path,include
from Zoo.views import main

urlpatterns = [
    path('', main.as_view(), name='home'),

]