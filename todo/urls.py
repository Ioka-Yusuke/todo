from django.urls import path
from . import views

urlpatterns = [
    path('', views.MyLoginView.as_view(), name="login"),
    path('logout/', views.MyLogoutView.as_view(), name="logout"),
    path('index/',views.index, name="index"),
    path('create/',views.UserCreateView.as_view(),name="create"),
    path('post/new/',views.post_new, name="post_new"),
    path('post/<int:pk>/delete_post/', views.delete_post, name='delete_post'),
    path('post/<int:pk>/important_rank/', views.important_rank, name='important_rank'),
]
