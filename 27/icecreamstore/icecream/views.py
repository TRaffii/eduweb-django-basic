from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .models import Icecream
from .serialize import IcecreamSerializer


def hello_view(request):
    return HttpResponse("Hello")

class IcecreamView(viewsets.ModelViewSet):
    serializer_class = IcecreamSerializer
    queryset = Icecream.objects.all()
