from django.urls import path

from .views import OtherPageView

urlpatterns = [
    path("", OtherPageView.as_view(), name="other"),
]
