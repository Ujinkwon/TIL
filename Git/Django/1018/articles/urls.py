from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('articles/',views.article_cr),
    path('articles/<int:article_pk>/', views.article_rud),
    path('comments/<int:comment_pk>/', views.comment_rud),
    path('articles/<int:article_pk>/comments/', views.comment_c),
]