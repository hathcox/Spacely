# -*- coding: utf-8 -*-
from spacely.models import Zone


def bootstrap():
    zone_check = Zone.objects.all()
    if zone_check:
        pass
    else:
        new_zone = Zone()
        new_zone.name = "zone-1"
        new_zone.save()
        print 'First zone created'
