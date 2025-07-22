
from django import forms
from .models import Ticket

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['imie', 'nazwisko', 'tytul', 'opis', 'miejsce']

class TicketLookupForm(forms.Form):
    identyfikator = forms.CharField(label="Identyfikator", max_length=4)
