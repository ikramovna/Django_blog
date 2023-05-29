from . import views
from django.urls import path

from .views import PostDetailView, SendEmailView

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('post_detail/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
    path('contact/', SendEmailView.as_view(), name='contact'),

]