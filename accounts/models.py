from __future__ import unicode_literals

from datetime import date

from django.contrib.auth.models import User
from django.db import models
from django.db.models import signals
from django.utils.translation import ugettext as _

from django_countries.fields import CountryField


optional = {'null': True, 'blank': True}


class Contact(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100, **optional)
    email = models.EmailField(**optional)
    contact_no = models.CharField(max_length=100)
    role = models.CharField(max_length=100)

    class Meta:
        verbose_name = _('Contact')
        verbose_name_plural = _('Contacts')

    def __unicode__(self):
        return '{} - {}'.format(self.name, self.contact_no)


class UserProfile(models.Model):
    GENDER_MALE = 'M'
    GENDER_FEMALE = 'F'
    GENDER_CHOICES = (
        (GENDER_MALE, _('Male')),
        (GENDER_FEMALE, _('Female')),
    )

    LEVEL_CHOICES = (
        (1, _('Grade 1')),
        (2, _('Grade 2')),
        (3, _('Grade 3')),
        (4, _('Grade 4')),
        (5, _('Grade 5')),
        (6, _('Grade 6')),
        (7, _('Grade 7 - Junior High School')),
        (8, _('Grade 8 - Junior High School')),
        (9, _('Grade 9 - Junior High School')),
        (10, _('Grade 10 - Senior High School')),
        (11, _('Grade 11 - Senior High School')),
        (12, _('Grade 12 - Senior High School')),
        (13, _('Undergraduate')),
        (14, _('Graduate')),
        (15, _('Masteral')),
        (16, _('Doctorate')),
    )

    CITY_CHOICES = (
        (_('Davao City'), _('Davao City')),
        (_('Tagum City'), _('Tagum City')),
        (_('Panabo City'), _('Panabo City')),
    )

    BLOOD_TYPES = (
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
    )

    # user = models.OneToOneField(User)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(**optional)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    age = models.PositiveSmallIntegerField(default=0)
    address = models.CharField(max_length=500, **optional)
    city = models.CharField(
        max_length=100,
        choices=CITY_CHOICES
    )
    # country = CountryField()
    mobile = models.CharField(max_length=30, **optional)

    level = models.SmallIntegerField(
        choices=LEVEL_CHOICES,
        verbose_name=(_('Grade or Year Level')),
    )
    course = models.CharField(
        max_length=30,
        verbose_name=_('Section or Degree'),
    )

    weight = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    wingspan = models.IntegerField(default=0)
    blood_type = models.CharField(
        max_length=3,
        choices=BLOOD_TYPES,
        **optional
    )

    emergency_contact = models.ForeignKey(Contact, **optional)

    class Meta:
        verbose_name = _('User Profile')
        verbose_name_plural = _('User Profiles')

    def get_fullname(self):
        middle_initial = '{}.'.format(
            self.middle_name[0]) if self.middle_name else ''
        return '{}, {} {}'.format(
            self.last_name,
            self.first_name,
            middle_initial,
        )

    def __unicode__(self):
        return self.get_fullname()


def calculate_age(sender, **kwargs):
    userprofile = kwargs.get('instance')

    today = date.today()
    born = userprofile.date_of_birth

    age = today.year - born.year - \
        ((today.month, today.day) < (born.month, born.day))

    UserProfile.objects.filter(id=userprofile.pk).update(age=age)

signals.post_save.connect(
    calculate_age,
    sender=UserProfile,
    dispatch_uid='userprofile-calcage-signal'
)


# -- Intermediary Tables -- #

class Waiver(models.Model):
    userprofile = models.ForeignKey(UserProfile)
    event = models.ForeignKey('events.Event', **optional)

    class Meta:
        verbose_name = _('Waiver')
        verbose_name_plural = _('Waivers')
        unique_together = ['userprofile', 'event',]

    def __unicode__(self):
        purpose = ' for {}'.format(self.event.name) if self.event else ''

        return 'Waiver of {} {}'.format(
            self.userprofile.get_fullname(),
            purpose,
        )
