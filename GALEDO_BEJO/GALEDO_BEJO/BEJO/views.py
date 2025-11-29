from django.shortcuts import render
from django.http import HttpResponse
from .models import childClass

# Create your views here.
def show_whole_data(request):
    dataClass = childClass.objects.all()

    return render(request, 'home.html', {'childClass':dataClass})