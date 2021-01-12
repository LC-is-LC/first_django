# Created for signaling

# signal that fires after an object is saved
from django.db.models.signals import post_save
# Since the post save fires when a user is created, we import user, which will be the sender
from django.contrib.auth.models import User
# Import what will receive the signal and run it
from django.dispatch import receiver
# since a profile will be created for each user in our function, we import profile
from .models import Profile

# create a function that creates a new profile for a user if the user is created
#a receiver decorator will be sent the User after it is saved (i.e post_save)
# kwargs just accept any additional keyword
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


# To make sure profiles are saved after made
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()