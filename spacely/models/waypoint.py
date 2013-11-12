# -*- coding: utf-8 -*-
from django.db import models
from ship import Ship


class Waypoint(models.Model):

    waypoints = models.ForeignKey('self')
    ship = models.ForeignKey(Ship)
    location_x = models.IntegerField('location_x')
    location_y = models.IntegerField('location_y')

    class Meta:
        app_label = 'spacely'
        db_table = 'waypoints'