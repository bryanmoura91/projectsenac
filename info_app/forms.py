from django import forms
from .models import Person

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'age']

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) < 3:
            raise forms.ValidationError("O nome deve ter pelo menos 3 caracteres.")
        return name

    def clean_age(self):
        age = self.cleaned_data['age']
        if not isinstance(age, int):
            raise forms.ValidationError("Idade deve ser um número.")
        if age > 150:
            raise forms.ValidationError("Idade máxima permitida é 150 anos.")
        return age
