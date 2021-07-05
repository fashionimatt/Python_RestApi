from django.http.response import HttpResponse, JsonResponse
#from django.shortcuts import render
#from django.views import View
from django.core import serializers
from django.forms.models import model_to_dict
from requests.models import MissingSchema
from restapiapp.models.base_model import TBoard
from restapiapp.serializers import tBoardSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
#from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView
from rest_framework.response import Response
import json

# Create your views here.

class Index(viewsets.ModelViewSet):
    queryset = TBoard.objects.all()
    serializer_class = tBoardSerializer

    @action(methods=['post'], detail=False) 
    def notice(self, request):
        print('====================================')
        print(request.data['queryString'])
        queryString = request.data['queryString']
        print('====================================')

        resDict = TBoard.objects.raw(queryString)

        for p in resDict :
            print(p.title)

        #resDict = resDict[0]

        print(resDict)
        print('====================================')

        #resDict = serializers.serialize('json', resDict)
        resDict = serializers.serialize('json', resDict)

        #print(resDict.values())
        print(json.dumps(resDict))
        print('====================================')

        return HttpResponse(json.dumps(resDict))

'''
class Index_Detail(RetrieveAPIView):
    lookup_field = 'brd_uid'
    queryset = t_board.objects.all()
    serializer_class = tBoardSerializer

class Index_Update(UpdateAPIView):
    queryset = t_board.objects.all()
    serializer_class = tBoardSerializer

class Index_Delete(DestroyAPIView):
    queryset = t_board.objects.all()
    serializer_class = tBoardSerializer

class Index_Insert(CreateAPIView):
    queryset = t_board.objects.all()
    serializer_class = tBoardInsertSerializer

'''

    