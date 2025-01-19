from django import forms
from .models import Enquiry  # Import the Enquiry model

class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = ['email', 'enquiry']  # Specify the fields you want in the form
