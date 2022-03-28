from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profile_api import views


router = DefaultRouter()
router.register(
    'sample-viewset',
    views.SampleViewSet,
    base_name='sample-viewset'
)
router.register('profile', views.UserProfileViewset)

urlpatterns = [
    path('sample-view/', views.SampleAPIView.as_view()),
    path('', include(router.urls))
]
