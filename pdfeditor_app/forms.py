from django import forms
from .models import Document

class UploadFileForm(forms.Form):
    pdf_file = forms.FileField()