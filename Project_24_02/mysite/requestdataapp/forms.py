from django import forms
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.exceptions import ValidationError

class UserBioForm(forms.Form):
    # file = forms.FileField()
    name = forms.CharField(max_length=100)
    age = forms.IntegerField(label="Your age", min_value=1, max_value=100)
    bio = forms.CharField(label='Biography', max_length=1000, widget=forms.Textarea)

def validate_file_name(file: InMemoryUploadedFile) -> None:
    if file.name and "virus" in file.name.lower():
        raise ValidationError("File name should not contain 'virus'")
class UploadFileForm(forms.Form):
    file = forms.FileField(validators=[validate_file_name])