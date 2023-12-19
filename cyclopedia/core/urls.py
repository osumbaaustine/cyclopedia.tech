from django.urls import path
from . import views


app_name = 'core'

urlpatterns = [
   path('', views.Index.as_view(), name='index'),

   path('ai/', views.AI.as_view(), name='AI'),
   path('<slug:slug>/', views.post_detail, name='post_detail'),
]
