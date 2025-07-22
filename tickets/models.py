
from django.db import models
from django.contrib.auth.models import User
import random

class Ticket(models.Model):
    STATUS_CHOICES = [
        ('open', 'Otwarte'),
        ('in_progress', 'W toku'),
        ('closed', 'Zamknięte'),
    ]

    imie = models.CharField(max_length=100)
    nazwisko = models.CharField(max_length=100)
    identyfikator = models.CharField(max_length=4, unique=True, editable=False, null=True, blank=True)
    tytul = models.CharField(max_length=200)
    opis = models.TextField()
    miejsce = models.CharField(max_length=200)
    data_utworzenia = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')
    przypisany_uzytkownik = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    komentarz = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.identyfikator:
            self.identyfikator = self.generate_unique_id()
        super().save(*args, **kwargs)

    def generate_unique_id(self):
        while True:
            kod = f"{random.randint(1000, 9999)}"
            if not Ticket.objects.filter(identyfikator=kod).exists():
                return kod

    def __str__(self):
        return f"{self.tytul} - {self.identyfikator}"
