from __future__ import unicode_literals

from django.db import models
from accounts.models import UserProfile, Contact
from django.utils.translation import ugettext as _

optional = {'null': True, 'blank': True}


class Affiliation(models.Model):
    AFFILIATION_TYPES = (
        (1, _('School')),
        (2, _('Foundation')),
        (3, _('Company')),
    )

    name = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    classification = models.IntegerField(
        choices=AFFILIATION_TYPES,
        **optional
    )
    members = models.ManyToManyField(
        UserProfile,
        related_name='Member',
        **optional
    )

    contact = models.ForeignKey(Contact, **optional)

    class Meta:
        verbose_name = _('Affiliation')
        verbose_name_plural = _('Affiliations')

    def __unicode__(self):
        return self.name
