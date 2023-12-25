from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
   path('', views.Index.as_view(), name='index'),
   path('upload-excel/', views.upload_excel, name='upload_excel'),
   path('ai/', views.AICategoryListView.as_view(), name='ai_category'),
   path('<slug:slug>/', views.entry_detail, name='entry_detail'),
]
