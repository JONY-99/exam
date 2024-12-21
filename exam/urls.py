from django.urls import path
from exam.views import home_view

urlpatterns =[
    path("", home_view, name='home' )
]
