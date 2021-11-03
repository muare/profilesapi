from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=240, blank=True)
    city = models.CharField(max_length=50, blank=True)
    avatar = models.ImageField(null=True, blank=True)

    def __str__(self) -> str:
        return self.user.username


class ProfileStatus(models.Model):
    user_profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="statuses")
    status_content = models.CharField(max_length=240, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(self.user_profile)

    class Meta:
        verbose_name_plural = "statuses"
