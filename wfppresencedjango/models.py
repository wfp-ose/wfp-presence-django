from django.db import models

from lsibdjango.models import GeographicThesaurusEntry
from gauldjango.models import GAULAdmin0

class WFPRegionalBureau(models.Model):
    """
    WFP Regional Bureaus
    """
    code = models.CharField(max_length=3)
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    opweb = models.IntegerField()

    def __str__(self):
        return "%s" % self.name.encode('utf-8')

    class Meta:
        ordering = ("code",)
        verbose_name = 'WFP Regional Bureau'
        verbose_name_plural = 'WFP Regional Bureaus'


class WFPCountry(models.Model):
    """
    WFP Country
    """
    thesaurus = models.ForeignKey(GeographicThesaurusEntry, db_index=True, null=True)
    gaul = models.ForeignKey(GAULAdmin0, db_index=True, null=True)
    regionalbureau = models.ForeignKey(WFPRegionalBureau, db_index=True, null=True)
    opweb = models.IntegerField(null=True)

    @property
    def iso_alpha2(self):
        if self.thesaurus_id:
            return GeographicThesaurusEntry.objects.filter(pk=self.thesaurus_id).values_list('iso_alpha2', flat=True)[0]
        else:
            return None

    @property
    def iso_alpha3(self):
        if self.thesaurus_id:
            return GeographicThesaurusEntry.objects.filter(pk=self.thesaurus_id).values_list('iso_alpha3', flat=True)[0]
        else:
            return None

    @property
    def name(self):
        if self.gaul_id:
            return GAULAdmin0.objects.filter(pk=self.gaul_id).values_list('admin0_name', flat=True)[0]
        else:
            return None

    @property
    def regionalbureau_name(self):
        if self.regionalbureau_id:
            return self.regionalbureau.name
        else:
            return None

    def __str__(self):
        if self.gaul_id:
            return "%s" % GAULAdmin0.objects.filter(pk=self.gaul_id).values_list('admin0_name', flat=True)[0].encode('utf-8')
        else:
            return ""

    class Meta:
        ordering = ("thesaurus__iso_alpha3",)
        verbose_name = 'WFP Country'
        verbose_name_plural = 'WFP Countries'
