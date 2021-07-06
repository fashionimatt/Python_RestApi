from django.urls import path, include
#from django.urls.conf import include
# from .views.base_view import Index
from rest_framework import routers
from .views import base_view

router = routers.DefaultRouter()
router.register(r'notices', base_view.Notices, basename='notices')
#router.register(r'notices/detail', base_view.Notices_Detail, basename='notices_detail')
#router.register(r'notices/<int:brd_uid>', base_view.Notices_Detail, basename='notices_detail')

urlpatterns = [
    path('api_auth/', include('rest_framework.urls')),
    path('', include(router.urls))
    #path('index/<int:brd_uid>', base_view.Index_Detail.as_view(), name='index_detail'),
    #path('index/<int:brd_uid>/update', base_view.Index_Update.as_view(), name='index_update'),
    #path('index/<int:brd_uid>/delete', base_view.Index_Delete.as_view(), name='index_delete'),
    #path('index/insert', base_view.Index_Insert.as_view(), name='index_insert'),
]
