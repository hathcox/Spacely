# -*- coding: utf-8 -*-
from django.db import models
from user import CustomUser


class Zone(models.Model):

    models.ForeignKey(CustomUser)
    name = models.TextField("name", max_length=128, blank=True)

    class Meta:
        app_label = 'spacely'
        db_table = 'zones'