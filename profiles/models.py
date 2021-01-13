from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

class UserProfile(models.Model):
    """ User Profile Model for deliver and history information """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(max_length=80, null=False, blank=True)
    default_country = CountryField(blank_label="Country", null=False, blank=True)
    default_postcode = models.CharField(max_length=80, null=False, blank=True)
    default_town_or_city = models.CharField(max_length=80, null=False, blank=True)
    default_street_address1 = models.CharField(max_length=80, null=False, blank=True)
    default_street_address2 = models.CharField(max_length=80, null=False, blank=True)
    default_county = models.CharField(max_length=80, null=False, blank=True)
    #default_email = models.CharField(max_length=80, null=False, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_delete(sender, instance, created, **kwargs):
    """ Create or delete a user profile """
    if created:
        UserProfile.objects.create(user=instance)
    # Existing user just save profile
    instance.userprofile.save()