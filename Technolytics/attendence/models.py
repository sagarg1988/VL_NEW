# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from instructor.models import Instructor

from student.models import Student


class Subject(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    student = models.ManyToManyField(Student, related_name='student_subject')
    instructor = models.ManyToManyField(Instructor, related_name='student_subject')


class Attendance(models.Model):
    final_scan_image = models.ImageField()
    final_scan_url = models.URLField()


class Video(models.Model):
    final_scan_image = models.ImageField()
    total_image = models.IntegerField()
    video_url = models.URLField()


class AttendanceScan(models.Model):
    final_scan_image = models.ImageField()
    total_image = models.IntegerField()
    url = models.URLField()
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='attendance_scan')
    attendance = models.ForeignKey(Attendance, on_delete=models.CASCADE, related_name='attendance_report')
    student = models.ManyToManyField(Student, related_name='student_attendance')


class Period(models.Model):
    start_time = models.DateTimeField('Start Time', default=None)
    end_time = models.DateTimeField('End Time', default=None)
    total_time = models.FloatField('Start Time', default=None)
    attendance = models.OneToOneField(Attendance, on_delete=models.CASCADE, related_name='period')
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, related_name='attendance_report')
    student = models.ManyToManyField(Student, related_name='student_period')

