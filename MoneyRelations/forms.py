from django import forms
from .models import Expense


class AppointmentForm(forms.ModelForm):

    class Meta:
        model = Expense
        fields = ['DateOfDocument', 'PaymentDate']

    appointment_date = forms.DateField(
        widget=forms.DateInput(format='%d/%m/%Y'),
        input_formats=('%d/%m/%Y', )
        )

class MyModelForm(forms.ModelForm):
    class Meta:
        model = Expense
        widgets = {
            'PaymentStatus': forms.BooleanField
        }

from django import forms

class CountryForm(forms.Form):
        OPTIONS = (
                ("AUT", "Austria"),
                ("DEU", "Germany"),
                ("NLD", "Neitherlands"),
                )
        Countries = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                             choices=OPTIONS)

