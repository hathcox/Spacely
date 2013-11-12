# -*- coding: utf-8 -*-
from django.db import models


class Projectile(models.Model):

    location_x = models.IntegerField('location_x')
    location_y = models.IntegerField('location_y')
    direction_x = models.IntegerField('direction_x')
    direction_y = models.IntegerField('direction_y')
    velocity_x = models.IntegerField('velocity_x')
    velocity_y = models.IntegerField('velocity_y')
    rotation_x = models.IntegerField('rotation_x')
    rotation_y = models.IntegerField('rotation_y')
    strength = models.IntegerField('strength')

    class Meta:
        app_label = 'spacely'
        db_table = 'projectiles'