from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
   path('', views.Index.as_view(), name='index'),
   path('upload-excel/', views.upload_excel, name='upload_excel'),
   path('ai/', views.AICategoryListView.as_view(), name='ai_category'),
   path('crypto/', views.CryptoCategoryListView.as_view(), name='crypto_category'),
   path('saas/', views.SAASCategoryListView.as_view(), name='saas_category'),
   path('blockchain/', views.BlockchainCategoryListView.as_view(), name='blockchain_category'),
   path('<slug:slug>/', views.entry_detail, name='entry_detail'),


]
