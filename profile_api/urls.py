from django.urls import path
from profile_api import views


urlpatterns = [
    path('sample_view/', views.SampleAPIView.as_view())
]
