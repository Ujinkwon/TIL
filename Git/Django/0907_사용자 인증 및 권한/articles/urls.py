from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<pk>/', views.detail, name='detail'),
    path('delete/<pk>/', views.delete, name='delete'),
    path('update/<pk>/', views.update, name='update'),
]
