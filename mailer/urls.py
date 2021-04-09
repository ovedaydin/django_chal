

from django.urls import path, include
from . import views


urlpatterns = [
    path('',views.home, name='home'),
    path('old',views.IndexView.as_view(), name='index'),
    path('company/<int:pk>',views.company, name='company'),
    path('companyAmount',views.companyAmount, name='companyAmount'),
    path('<int:page>',views.main, name='main'),
    path('add',views.form, name='form'),

    ]
