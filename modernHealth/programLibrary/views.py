from .models import Program
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .serializers import ProgramSerializer
from .pyrebase_settings import db, auth
from django.shortcuts import render

import json


@csrf_exempt
def getProgram(request, program_name):
    if request.method != 'GET':
        return HttpResponse(json.dumps({'Status': '405 Method Not Allowed'}), status=405)

    program = (Program.objects.filter(name=program_name.lower()))
    if not program.exists():
        return HttpResponse(json.dumps({'Status': 'Program name does not exist'}), status=400)

    data = ProgramSerializer(program, many=True).data
    return HttpResponse(json.dumps(data), status=200)


def helloWorld(request):
    return HttpResponse(json.dumps({'Status': 'Hello Django World!'}), status=200)


def get_rabbits(request):
    rabbits = db.child('rabbits').get()
    return HttpResponse(rabbits.val(), status=200)

def add_rabbit(request):
    data = {"name": "rabbit1", "isFluffy": True}
    db.child("rabbits").push(data)

    return HttpResponse(json.dumps(data), status=200)