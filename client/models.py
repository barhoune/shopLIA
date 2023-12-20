from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    GENRE_CHOICES = (
        ('H', 'Homme'),
        ('F', 'Femme'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    first_name = models.CharField(max_length=30, default="")
    last_name = models.CharField(max_length=30, default="")
    email = models.EmailField(max_length=150, default="")
    address = models.CharField(max_length=150, default="")
    password = models.CharField(max_length=10, default="")
    gender=models.CharField(max_length=1, choices=GENRE_CHOICES, default="H")
    active=models.BooleanField(default=True)
    def __str__(self):
        return self.user.username
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(
            user=instance,
            first_name=instance.first_name,
            last_name=instance.last_name,
            email=instance.email,
            )

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()