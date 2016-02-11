from django.contrib import admin

from wfppresencedjango.models import  WFPRegionalBureau, WFPCountry

class WFPRegionalBureauAdmin(admin.ModelAdmin):
    model = WFPRegionalBureau
    list_display_links = ('name',)
    list_display = ('code', 'name', 'city', 'opweb', )

class WFPCountryAdmin(admin.ModelAdmin):
    model = WFPCountry
    list_display_links = ('name',)
    list_display = ('iso_alpha3', 'name', 'regionalbureau_name', )
    # Django will do a full select on the gaul to load it for
    # changing the reference pointer.  This is incredibly slow, because
    # it will load all of the geometry in mpoly.  With raw_id_fields,
    # Django will only run a simply query against gaul for the name.
    # https://docs.djangoproject.com/en/dev/ref/contrib/admin/#django.contrib.admin.ModelAdmin.raw_id_fields
    # http://www.lexev.org/en/2013/django-admin-site-optimisation/
    raw_id_fields = ("gaul",)

admin.site.register(WFPRegionalBureau, WFPRegionalBureauAdmin)
admin.site.register(WFPCountry, WFPCountryAdmin)
