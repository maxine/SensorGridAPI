# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# template for sensor grid data
class SensorData(models.Model):
    battery = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    created_at = models.DateTimeField(null=True)
    data = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    data_type = models.CharField(max_length=100, blank=True, default='')
    message_id = models.IntegerField(null=True)
    network = models.IntegerField(null=True)
    node_id = models.IntegerField(null=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=7, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=7, null=True)
    ram = models.IntegerField(null=True)
    recieved_at = models.DateTimeField(auto_now_add=True)
    record_id = models.CharField(max_length=100, blank=True, default='')
    timestamp = models.DateTimeField(auto_now_add=True)
    version = models.IntegerField(null=True)

    class Meta:
        ordering = ('id',)
