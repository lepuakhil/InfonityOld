from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.models import Group




def customer_profile(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='site_engineer')
        instance.groups.add(group)

        Profile.objects.create(
            user=instance,
            full_name=instance.first_name + ' ' + instance.last_name
        )
        print('Profile created')


post_save.connect(customer_profile, sender=User)