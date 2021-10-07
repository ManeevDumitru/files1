from django.http import HttpResponse
from django.core import serializers
from tasks.models import Company


def index(request):
    return HttpResponse(serializers.serialize('json',Company.objects.all()))