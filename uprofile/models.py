from django.db import models
from accounts.models import Account
from django.dispatch import receiver
from django.db.models.signals import post_save


def get_profile_image_filepath(self, filename):
    return 'profile_images/' + str(self.pk) + '/profile_image.png'

def get_default_profile_image():
    return "codingwithdk/dummy_robort.png"

class Profile(models.Model):
    username = models.OneToOneField(Account, on_delete=models.CASCADE, null=True, blank=True,related_name='profile')
    first_name = models.CharField(max_length=20,null=True, blank=True)
    last_name = models.CharField(max_length=20,null=True, blank=True)
    address = models.CharField(max_length=200,null=True, blank=True)
    phone = models.CharField(max_length=50,null=True, blank=True)
    profile_image = models.ImageField(max_length=200, upload_to=get_profile_image_filepath,  null=True, blank=True, default=get_default_profile_image)

    def __str__(self):
        return str(self.username)
    
    def get_profile_image_filename(self):
        return str(self.profile_image)[str(self.profile_image).index('profile_images/' + str(self.pk) + "/"):]

@receiver(post_save, sender=Account)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(username=instance)
        print('Profile created')

@receiver(post_save, sender=Account)
def save_profile(sender, instance, created, **kwargs):
    if created == False:
        instance.profile.save()
        print('Profile updated')