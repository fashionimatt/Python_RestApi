from .models.base_model import TBoard
from rest_framework import serializers

class tBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = TBoard
        fields = ('brd_uid', 'title', 'cntnt', 'rgst_dttm', 'updt_dttm')

'''
class tBoardInsertSerializer(serializers.ModelSerializer):
    class Meta:
        model = t_board
        fields = ('title', 'cntnt', 'rgst_dttm', 'updt_dttm')
'''