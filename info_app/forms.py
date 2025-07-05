from django import forms
from .models import Person, ContactLog


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'age', 'gender']

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


class FeedbackForm(forms.Form):
    SATISFACTION_CHOICES = [
        ('Excelente', 'Excelente'),
        ('Bom', 'Bom'),
        ('Regular', 'Regular'),
        ('Ruim', 'Ruim'),
    ]

    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail')
    comentario = forms.CharField(label='Comentário', widget=forms.Textarea)
    satisfacao = forms.ChoiceField(label='Satisfação', choices=SATISFACTION_CHOICES)


class ContactLogForm(forms.ModelForm):
    class Meta:
        model = ContactLog
        fields = ['person', 'message']
