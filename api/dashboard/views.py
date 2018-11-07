from django.shortcuts import render
from rest_framework import (response, schemas, filters, generics, viewsets,
                        views)
from django.http import JsonResponse
from pymongo import MongoClient
import datetime
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.parsers import JSONParser
from rest_framework.generics import GenericAPIView
from django.conf import settings
from bson import Binary
from bson.json_util import dumps
import time
# Create your views here.

@api_view(["POST"])
def crearUsuario(request):
    if request.method == "POST":
        client = MongoClient(settings.HOSTARDU, int(settings.PORTARDU))
        db = client["api_arduino"]
        db.authenticate(settings.USERARDU, settings.PASS)
        data = JSONParser().parse(request)
        usuarios = db['usuarios']

        idUser = int((time.time()*1000) % 86400000)
        data['idUsuario']= idUser
        result = usuarios.insert(data)
        respo = {
        "MongoObjectID": str(result),
        "Message": "nuevo objeto en la base de datos"
        }
        client.close()
        return JsonResponse(respo, safe=False)


@api_view(["POST", "GET"])
def canales(request):
    result = []
    if request.method == "GET":
        client = MongoClient(settings.HOSTARDU, int(settings.PORTARDU))
        db = client["api_arduino"]
        db.authenticate(settings.USERARDU, settings.PASS)
        canales = db['canales']
        data = canales.find({})

        for dto in data:
            json_data = {
                "idArduino": dto["idArduino"],
                "nombre": dto['nombre'],
                'dueno': dto['dueno'],
                'descripcion': dto['descripcion']
            }
            result.append(json_data)
        client.close()
        return JsonResponse(result, safe=False)

    if request.method == "POST":
        client = MongoClient(settings.HOSTARDU, int(settings.PORTARDU))
        db = client["api_arduino"]
        db.authenticate(settings.USERARDU, settings.PASS)
        canales = db['canales']
        data = JSONParser().parse(request)
        idArduino = int((time.time()*1000) % 86400000)
        data['idArduino']= idArduino
        result = canales.insert(data)
        respo = {
            "MongoObjectID": str(result),
            "Message": "nuevo objeto en la base de datos"
        } 
        client.close()
        return JsonResponse(respo, safe=False)

@api_view(["POST", "GET", "DELETE"])
def canalDetail(request, pk, format=None):
    if request.method == "GET":
        result = []
        client = MongoClient(settings.HOSTARDU, int(settings.PORTARDU))
        db = client["api_arduino"]
        db.authenticate(settings.USERARDU, settings.PASS)
        canales = db['canales']
        data = canales.find({"idArduino": int(pk)})
        jsonData={"holaaa": "asdd"}
        for dto in data:
            jsonData ={
                "idArduino": int(pk),
                "nombre": dto['nombre'],
                'dueno': dto['dueno'],
                'descripcion': dto['descripcion']
            }   
            result.append(jsonData)
        client.close()
        return JsonResponse(jsonData, safe=False)
    
    if request.method == "POST":
        client = MongoClient(settings.HOSTARDU, int(settings.PORTARDU))
        db = client["api_arduino"]
        db.authenticate(settings.USERARDU, settings.PASS)
        canales = db['canales']
        d = JSONParser().parse(request)
        data = canales.update({"idArduino":int(pk)}, {
            "idArduino": int(pk),
            "nombre": d['nombre'],
            "dueno": d['dueno'],
            "descripcion": d['descripcion']
        })
        respo = {
            "MongoObjectId": str(data),
            "Message": "Objeto ha sido actualizado"
        }
        client.close
        return JsonResponse(respo, safe=False)

    if request.method == "DELETE":
        client = MongoClient(settings.HOSTARDU, int(settings.PORTARDU))
        db = client["api_arduino"]
        db.authenticate(settings.USERARDU, settings.PASS)
        canales = db['canales']
        result = canales.remove({"idArduino": int(pk)})
        respo = {
            "MongoObjectID": str(result),
            "Message": "Objeto ha sido borrado"
        } 
        client.close()
        return JsonResponse(respo, safe=False)

@api_view(["POST", "GET"])
def recursos(request):
    if request.method == "GET":
        result =[]
        client = MongoClient(settings.HOSTARDU, int(settings.PORTARDU))
        db = client["api_arduino"]
        db.authenticate(settings.USERARDU, settings.PASS)
        recursos = db['recursos']
        data = recursos.find({})
        for dto in data:
            jsonData = {
                "idRecurso": dto["idRecurso"],
                "nombre": dto["nombre"],
                "unidad": dto["unidad"],
                "descripcion": dto["descripcion"],
                "medidas": dto["medidas"],
                "dueno": dto["dueno"]
            }
            result.append(jsonData)
        client.close()
        return JsonResponse(result, safe=False)
    
    if request.method == "POST":
        client = MongoClient(settings.HOSTARDU, int(settings.PORTARDU))
        db = client["api_arduino"]
        db.authenticate(settings.USERARDU, settings.PASS)
        recursos = db['recursos']
        data = JSONParser().parse(request)
        idRecurso = int((time.time()*1000) % 86400000)
        data['idRecurso']= idRecurso
        result = recursos.insert(data)
        respo = {
            "MongoObjectID": str(result),
            "Message": "nuevo objeto en la base de datos"      
        }
        return JsonResponse(respo, safe=False)


@api_view(["GET"])
def recursosDetail(request, pk):
    if request.method == "GET":
        result = []
        client = MongoClient(settings.HOSTARDU, int(settings.PORTARDU))
        db = client["api_arduino"]
        db.authenticate(settings.USERARDU, settings.PASS)
        recursos = db['canales']
        data = recursos.find({"idRecurso": int(pk)})
        jsonData={"holaaa": "asdd"}
        for dto in data:
            jsonData ={
                "idRecurso": int(pk),
                "nombre": dto['nombre'],
                "unidad": dto["unidad"],
                "descripcion": dto["descripcion"],
                "medidas": dto["medidas"],
                "dueno": dto["dueno"]
            }   
            result.append(jsonData)
        client.close()
        return JsonResponse(jsonData, safe=False)


@api_view(["POST"])
def registrarMedida(request, pk):
    if request.method == "POST":
        client = MongoClient(settings.HOSTARDU, int(settings.PORTARDU))
        db = client["api_arduino"]
        db.authenticate(settings.USERARDU, settings.PASS)
        recursos = db['recursos']



        







            


