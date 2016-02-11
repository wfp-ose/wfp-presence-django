import autocomplete_light.shortcuts as autocomplete_light

from wfppresencedjango.models import WFPRegionalBureau, WFPCountry

class WFPRegionalBureauAutocomplete(autocomplete_light.AutocompleteGenericBase):
    search_fields=['^name']
    model=WFPRegionalBureau
    attrs={
        'placeholder': 'Other model name ?',
        'data-autocomplete-minimum-characters': 1
    }
    widget_attrs={
        'data-widget-maximum-values': 4,
        'class': 'modern-style'
    }


class WFPCountryAutocomplete(autocomplete_light.AutocompleteGenericBase):
    search_fields=['^name']
    model=WFPCountry
    attrs={
        'placeholder': 'Other model name ?',
        'data-autocomplete-minimum-characters': 1
    }
    widget_attrs={
        'data-widget-maximum-values': 4,
        'class': 'modern-style'
    }


autocomplete_light.register(WFPRegionalBureauAutocomplete)
autocomplete_light.register(WFPCountryAutocomplete)
