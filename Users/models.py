from django.db import models
from PIL import Image
# #LC Importing the normal django user model
from django.contrib.auth.models import User
# #LC extending the normal django user model and adding other fields like profile picture


class Profile(models.Model):
    # Creating a ONE TO ONE relationship with the normal User model, so we pass in the User model
    # Cascade to delete the profile of a user when user is deleted
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # default.jpg is the default image before it is changed to a new image which will be uploaded to profile_pics
    # default.jpg will be the picture you drop in the directory it will create
    # the upload_to directory will be created
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    # to show what will represent a Profile whenever it is made

    def __str__(self):
        return f'{(self.user.username).capitalize()}\'s Profile'

    # Editing the save function, to resize the new images (profile pics) when saved
    def save(self, *args, **kwargs):
        # firstly make sure the normal save of the parent class happens so the new image is saved
        super().save(*args, **kwargs)
        # Then take the saved image then resize, using pillow, imported above

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)