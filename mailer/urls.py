

from django.urls import path, include
from . import views


urlpatterns = [
    path('',views.IndexView.as_view(), name='index'),
    path('company/<int:pk>',views.company, name='company'),

    ]
