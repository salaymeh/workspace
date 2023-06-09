from django.urls import path

from .views import BlogDetailView
from .views import BlogListView

urlpatterns = [
    path("", BlogListView.as_view(), name="home"),
    path("post/<int:pk>/", BlogDetailView.as_view(), name="post_detail"),
]
