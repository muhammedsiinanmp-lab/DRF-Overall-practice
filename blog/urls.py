from django.urls import path
from . import views

urlpatterns = [
    path('posts/',views.PostList.as_view()),
    path('posts/<slug:slug>/',views.PostDetail.as_view())
]