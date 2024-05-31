from django import forms
from .models import Rapport, Departement, Personnel

class RapportForm(forms.ModelForm):
    class Meta:
        model = Rapport
        fields = ['sujet', 'rapport_pdf', 'departement', 'personnel', 'date_defendu']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['departement'].queryset = Departement.objects.all()
        self.fields['personnel'].queryset = Personnel.objects.all()


