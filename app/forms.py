from app.models import Coordinates
from django import forms


class CoordinatesForm(forms.ModelForm):

    class Meta:
        model = Coordinates
        fields = ['address', ]
