# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Subject, AttendanceScan, Attendance, Video, Period


admin.site.register(Subject)
admin.site.register(Attendance)
admin.site.register(AttendanceScan)
admin.site.register(Video)
admin.site.register(Period)
# Register your models here.
