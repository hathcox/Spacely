# -*- coding: utf-8 -*-
from django.db import models
from django.contrib import auth


class CustomUser(auth.models.AbstractUser):

    biography = models.TextField('biography', blank=True)
    phone_number = models.CharField("phone_number", max_length=12)
    date_of_birth = models.CharField("date_of_birth", max_length=10)

    class Meta:
        app_label = 'spacely'
        db_table = 'user'


class UserManager(models.Manager):

    def __init__(self):
        super(UserManager, self).__init__()

    def create_user(self, username, password=None, email=None):
        """
        Creates and saves a User with the given userid, accesstoken,
        firstname, lastname and password.
        """
        user = CustomUser()
        user.username = username
        user.set_password(password)
        user.email = email
        user.save(using=self._db)
        return user
