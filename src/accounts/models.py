from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_resized import ResizedImageField
import random

"""
At the start please be careful to start migrations
--------------------------------------------------

STEP: 1 comment current_subscription [FIELD] in model [USER]
STEP: 1 py manage.py make migrations accounts
STEP: 2 py manage.py migrate
Then do next ...

"""


class User(AbstractUser):

    profile_image = ResizedImageField(
        upload_to='accounts/images/profiles/', null=True, blank=True, quality=100, force_format='PNG',
        help_text='size of logo must be 100*100 and format must be png image file', crop=['middle', 'center']
    )
    phone_number = models.CharField(max_length=19, null=True, blank=True)

    class Meta:
        ordering = ['-id']
        verbose_name = 'User Account'
        verbose_name_plural = 'Users Accounts'

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        self.matching = random.randint(50, 100)
        super(User, self).save(*args, **kwargs)