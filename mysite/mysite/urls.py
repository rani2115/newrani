
from django.contrib import admin
from django.urls import path
from like import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('like/', views.like_view, name='like'),
    path('likes/', views.showLikes, name='likes'),
]
