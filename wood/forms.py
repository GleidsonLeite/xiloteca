import django_filters
from django import forms
from .models import madeira

class searchWoodForm(forms.ModelForm):
    def __init__(self,  *args, **kwargs):
        # first call parent's constructor
        super().__init__(*args, **kwargs)
        # there's a `fields` property now
        #self.fields['__all__'].required = False
        self.fields['nomeCientifico'].required = False
        for i in self.fields:
            self.fields[i].required = False

    class Meta:
        model = madeira
        fields = '__all__'

class filterWood(django_filters.FilterSet):
    class Meta:
        model = madeira
        fields = {  'nomeCientifico',
                    'nomeVulgar',
                    'familia',
                    'cor',
                    'cheiro_carac',
                    'textura',
                    'peso',
                    'tipo_parenquima',
                    'dist_poros',
                    'tam_poros',
                    'qnt_poros',
                    'disp_poros',
                    'poros_cadeiasR',
                    'poros_obsT',
                    'con_ol_res',
                    'raioP_trans',
                    'raioP_tang',
                    'canais_secrt', }