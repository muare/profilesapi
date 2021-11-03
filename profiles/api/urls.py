from django.urls import path, include
from profiles.api.views import ProfileViewSet, AvatarUpdateAPIView,ProfileStatusViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'profiles', ProfileViewSet)
router.register(r'statuses', ProfileStatusViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('avatar/', AvatarUpdateAPIView.as_view(), name='avatar-update'),
]
