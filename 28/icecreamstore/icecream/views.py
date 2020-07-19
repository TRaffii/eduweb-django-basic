import random

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .models import Icecream
from .serialize import IcecreamSerializer


def hello_view(request):
    return HttpResponse("Hello")


def get_random_icecream(request):
    items = Icecream.objects.all()
    id = random.randrange(1, Icecream.objects.all().count())
    icecream = Icecream.objects.get(id=items[id].id)

    return JsonResponse({'icecream': icecream.name})

def get_featured_taste(request):
    icecream = Icecream.objects.filter(is_featured=True)

    return JsonResponse({'icecream': icecream.name})

class IcecreamView(viewsets.ModelViewSet):
    serializer_class = IcecreamSerializer
    queryset = Icecream.objects.all()


