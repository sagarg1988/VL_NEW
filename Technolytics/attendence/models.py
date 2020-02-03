# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Period(models.Model):
    start_time = models.DateTimeField('Start Time', default=None)
    end_time = models.DateTimeField('End Time', default=None)
    total_time = models.FloatField('Start Time', default=None)


class Subject(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)


class Attendance(models.Model):
    final_scan_image = models.ImageField()
    final_scan_url = models.URLField()


class AttendanceScan(models.Model):
    final_scan_image = models.ImageField()
    total_image = models.IntegerField()
    url = models.URLField()


class Video(models.Model):
    final_scan_image = models.ImageField()
    total_image = models.IntegerField()
    video_url = models.URLField()
