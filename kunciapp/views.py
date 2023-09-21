from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Anggota
from .serializers import AnggotaSerializer
from rest_framework.permissions import IsAuthenticated

class AnggotaViewSet(viewsets.ModelViewSet):
  queryset = Anggota.objects.all()
  serializer_class = AnggotaSerializer
  permission_classes = [IsAuthenticated]
  
  def create(self, request, *args, **kwargs):
    serializer = AnggotaSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      response = {
        'status': 'success',
        'code': status.HTTP_200_OK,
        'message': 'Data Anggota Berhasil ditambahkan',
        'files': serializer.data,
      }
      return Response(response)
    else :
      response = {
        'status': 'Bad Request',
        'code': status.HTTP_400_BAD_REQUEST,
        'message': 'Harus Login Untuk Menambah Content Ini',
      }
      return Response(response)
    
  def update(self, request, *args, **kwargs):
    partial = kwargs.pop('partial', True)
    instance = self.get_queryset()
    serializer = AnggotaSerializer(instance, data=request.data, partial=partial)
    if serializer.is_valid():
      serializer.save()
      response = {
        'status': 'success',
        'code': status.HTTP_200_OK,
        'message': 'Anggota Berhasil diperbaharui',
      }
      return Response(response)
    else:
      response = {
        'status': 'bad request',
        'code': status.HTTP_400_BAD_REQUEST,
        'message': 'Harus Login untuk mengubah data',
      }
      return Response(response)
    
  def destroy(self, request, *args, **kwargs):
    instance = self.get_queryset()
    instance.delete()
    
    response = {
      'status': 'success',
      'code': status.HTTP_204_NO_CONTENT,
      'message': 'Anggota Berhasil dihapus'
    }
    return Response(response)