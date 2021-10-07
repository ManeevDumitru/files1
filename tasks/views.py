from django.http import HttpResponse
from django.core import serializers
from tasks.models import Company
from django.views.decorators.csrf import csrf_exempt
from .services import *


def index(request):
    return HttpResponse(serializers.serialize('json', Company.objects.all()))


def detail(request, question_id):
    return HttpResponse(serializers.serialize('json', [Company.objects.get(pk=question_id)]))


@csrf_exempt
def create(request):
    print(request.POST)
    company = Company(
        name=request.POST.get("name"),
        website=request.POST.get("website"),
        totalEmployees=request.POST.get("totalEmployees"),
    )
    company.save()
    return HttpResponse(status=201)


@csrf_exempt
def destroy(request, question_id):
    delete_company(question_id)
    return HttpResponse(status=204)