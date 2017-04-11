from __future__ import unicode_literals

from datetime import datetime

from django.db import models
from django.utils.translation import ugettext as _

from accounts.models import UserProfile
from affiliations.models import Affiliation

optional = {'null': True, 'blank': True}


class Event(models.Model):
    name = models.CharField(max_length=255, **optional)
    description = models.TextField(**optional)

    organizer = models.ForeignKey(Affiliation, **optional)
    location = models.CharField(max_length=255, **optional)

    start = models.DateTimeField(default=datetime.utcnow)
    end = models.DateTimeField(default=datetime.utcnow)

    participants = models.ManyToManyField(
        UserProfile,
        related_name='Participants',
        **optional
    )

    class Meta:
        verbose_name = _('Event')
        verbose_name_plural = _('Events')

    def __unicode__(self):
        return self.name
