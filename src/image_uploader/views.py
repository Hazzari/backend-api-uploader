from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from src.base.services import save_file
from . import serializers


class ImageViewSet(APIView):
    """ Загрузка файлов изображений
    """
    serializer_class = serializers.FileListSerializer
    permission_classes = [permissions.IsAuthenticated, ]

    def post(self, request, format=None):
        img_serializer = self.serializer_class(data=request.data)
        if img_serializer.is_valid():
            for x in img_serializer.validated_data.get('image'):
                save_file(x)
        else:
            err = img_serializer.errors.get('image')
            return Response(data=err,
                            status=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)

        return Response('OK')
