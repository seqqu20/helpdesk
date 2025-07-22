
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import TicketForm, TicketLookupForm
from .models import Ticket

def home(request):
    return render(request, 'home.html')

def create_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save()
            return HttpResponse(f"Zgłoszenie zapisane. Twój identyfikator: {ticket.identyfikator}")
    else:
        form = TicketForm()
    return render(request, 'create_ticket.html', {'form': form})

def lookup_ticket(request):
    ticket = None
    not_found = False

    if request.method == 'POST':
        form = TicketLookupForm(request.POST)
        if form.is_valid():
            identyfikator = form.cleaned_data['identyfikator']
            try:
                ticket = Ticket.objects.get(identyfikator=identyfikator)
            except Ticket.DoesNotExist:
                not_found = True
    else:
        form = TicketLookupForm()

    return render(request, 'lookup_ticket.html', {
        'form': form,
        'ticket': ticket,
        'not_found': not_found
    })
