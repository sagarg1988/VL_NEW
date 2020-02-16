# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Student(models.Model):
    firstName = models.CharField(max_length=30, blank=True, null=True)
    lastName = models.CharField(max_length=30, blank=True,null=True)

    def __str__(self):
        return self.firstName + ": " + self.lastName
