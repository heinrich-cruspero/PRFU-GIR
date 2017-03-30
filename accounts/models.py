from __future__ import unicode_literals

from datetime import date

from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext as _

# from events.models import Event

from django_countries.fields import CountryField

optional = {'null': True, 'blank': True}


class UserProfile(models.Model):
    GENDER_MALE = 'M'
    GENDER_FEMALE = 'F'
    GENDER_CHOICES = (
        (GENDER_MALE, _('Male')),
        (GENDER_FEMALE, _('Female')),
    )

    user = models.OneToOneField(User)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, **optional)
    date_of_birth = models.DateField(**optional)
    address = models.CharField(max_length=500, **optional)
    city = models.CharField(max_length=100)
    country = CountryField()

    weight = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    wingspan = models.IntegerField(default=0)

    # Attendance
    # events = models.ForeignKey(Event, related_name='participant', **optional)


    class Meta:
        verbose_name = _('User Profile')
        verbose_name_plural = _('User Profiles')

    def __unicode__(self):
        if self.user.last_name and self.user.first_name:
            return "{}, {}".format(self.user.last_name, self.user.first_name)
        return  self.user.username

    def calculate_age(self):
        today = date.today()
        born = self.date_of_birth

        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
