from django.urls import path , include
from . import views
from django.views.generic import TemplateView
import os
app_name = 'core'

urlpatterns = [
  path('' , views.MainView.as_view(), name='index'),
   path('accounts/', include('django.contrib.auth.urls')),
  path('add' , views.riskCreate.as_view() , name='riskCreate'),
  path('<int:pk>/edit' , views.riskUpdate.as_view() , name='riskUpdate'),
  path('<int:pk>/delete' , views.riskDelete.as_view() , name='riskDelete'),
]