# -*- coding: utf-8 -*-
from django.db import models
from zone import Zone


class Planet(models.Model):

    zone = models.ForeignKey(Zone)
    size = models.IntegerField('size')
    location_x = models.IntegerField('location_x')
    location_y = models.IntegerField('location_y')
    direction_x = models.IntegerField('direction_x')
    direction_y = models.IntegerField('direction_y')

    name = models.TextField("name", max_length=128, blank=True)

    class Meta:
        app_label = 'spacely'
        db_table = 'planets'