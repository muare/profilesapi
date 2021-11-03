from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from profiles.api.permissions import IsOwnerOrReadOnly, IsOwnerProfileOrReadOnly
from profiles.api.serializers import (ProfileAvatarSerializer,
                                      ProfileSerializer,
                                      ProfileStatusSerializer)
from profiles.models import Profile, ProfileStatus


class ProfileViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]


class AvatarUpdateAPIView(UpdateAPIView):
    serializer_class = ProfileAvatarSerializer

    def get_object(self):
        return self.request.user.profile


class ProfileStatusViewSet(ModelViewSet):
    queryset = ProfileStatus.objects.all()
    serializer_class = ProfileStatusSerializer
    permission_classes = [IsAuthenticated, IsOwnerProfileOrReadOnly]

    def perform_create(self, serializer):
        user_profile = self.request.user.profile
        serializer.save(user_profile=user_profile)
