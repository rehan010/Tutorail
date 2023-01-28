from django import forms as _
from .models import *
class ContactForm(_.ModelForm):
    first_name=_.CharField(required=True)
    last_name=_.CharField(required=True)
    class Meta:
        model=Contact
        fields=('first_name','last_name')
        widgets={
            'first_name':_.TextInput(attrs={'class':'form-control'}),
            'last_name':_.TextInput(attrs={'class':'form-control'})
        }

    def clean(self):
        cleaned_data = super(ContactForm, self).clean()

        if any(self.errors):
            return self.errors

