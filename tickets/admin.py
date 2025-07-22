
from django.contrib import admin
from .models import Ticket

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('lp', 'tytul', 'status', 'przypisany_uzytkownik', 'data_utworzenia')
    list_filter = ('status', 'przypisany_uzytkownik')
    search_fields = ('tytul', 'nazwisko', 'identyfikator')
    ordering = ['-data_utworzenia']
    list_editable = ('status', 'przypisany_uzytkownik')

    fieldsets = (
        ('Podstawowe dane', {
            'fields': ('imie', 'nazwisko', 'tytul', 'opis', 'miejsce')
        }),
        ('Zarządzanie', {
            'fields': ('status', 'przypisany_uzytkownik', 'komentarz')
        }),
    )

    def lp(self, obj):
        return obj.pk
    lp.short_description = "LP"
