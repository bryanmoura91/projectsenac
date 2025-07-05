from django.db import models

class Person(models.Model):
    GENDER_CHOICES = [
        ('male', 'Masculino'),
        ('female', 'Feminino'),
        ('other', 'Outro'),
    ]

    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default='other')

    def __str__(self):
        return self.name

class ContactLog(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    message = models.TextField()

    def __str__(self):
        return f'Contato de {self.person.name} em {self.timestamp.strftime("%Y-%m-%d %H:%M")}'

