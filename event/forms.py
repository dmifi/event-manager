from django import forms

from .models import EventUsersData


class EventUsersDataForm(forms.ModelForm):
    description = forms.CharField(label='Описание',
                                  widget=forms.Textarea(),
                                  max_length=250)
    weight_user = forms.IntegerField(label="Масса",
                                     widget=forms.NumberInput(
                                         attrs={'onblur': 'sumTotal();'}))
    age_user = forms.IntegerField(label="Возраст",
                                  widget=forms.NumberInput(
                                      attrs={'onblur': 'sumTotal();'}))

    class Meta:
        model = EventUsersData
        fields = ['weight_user', 'age_user', 'text_a', 'text_b',
                  'description']
