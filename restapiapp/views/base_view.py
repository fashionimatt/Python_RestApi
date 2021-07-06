from django.http.response import HttpResponse
from django.core import serializers
from requests.models import MissingSchema
from restapiapp.models.base_model import TBoard
from restapiapp.serializers import tBoardSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
import pymysql

# Create your views here.
t_board = pymysql.connect(
        user = 'root', 
        passwd = 'mbaro2014', 
        host = 'valar.site',
        port = 3307, 
        db = 'test', 
        charset='utf8'
        )

cursor = t_board.cursor(pymysql.cursors.DictCursor)

class Notices(viewsets.ModelViewSet):
    queryset = TBoard.objects.all()
    serializer_class = tBoardSerializer

    # 주석 추가
    @action(methods=['POST'], detail=False) 
    def all(self, request):
        queryString = request.data['queryString']
        cursor.execute(queryString)
        result = cursor.fetchall()

        return HttpResponse(result, content_type="text/json-comment-filtered")

    @action(methods=['POST'], detail=False) 
    def details(self, request):
        queryString = request.data['queryString']
        cursor.execute(queryString)
        result = cursor.fetchall()

        return HttpResponse(result, content_type="text/json-comment-filtered")

    @action(methods=['POST'], detail=False) 
    def write(self, request):
        queryString = request.data['queryString']
        
        cursor.execute(queryString)
        t_board.commit()

        return HttpResponse()

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

    