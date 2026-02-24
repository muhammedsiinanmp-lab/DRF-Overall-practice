from django.db.models.signals import post_delete,post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save,sender=User)
def user_created_signal(sender,instance,created,**kwargs):
    if created:
        print(f'User {instance.username} created')
