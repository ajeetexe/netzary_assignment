
from django.forms import ModelForm, DateInput, NumberInput
from .models import CalcualteInterstModel


class CalculateInteresForm(ModelForm):
    class Meta:
        model = CalcualteInterstModel
        fields = '__all__'
        widgets = {
            'start_date': DateInput(attrs={'type':'date','class':'date'}),
            'end_date': DateInput(attrs={'type':'date','class':'date'}),
            'principal': NumberInput(attrs={'class':'principal'})
        }