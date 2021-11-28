from django.core.exceptions import ValidationError
from rest_framework import serializers, status

from src.base.services import validate_img


class FileListSerializer(serializers.Serializer):
    image = serializers.ListField(
        child=serializers.FileField(max_length=100000,
                                    allow_empty_file=False,
                                    use_url=False))

    def validate_image(self, files):
        """ Валидатор файлов
        """

        invalid_files: list = []

        for file in files:
            validate = validate_img(file)
            if not validate[0]:
                invalid_files.append((f'{file}', validate[1]))
        if invalid_files:
            raise ValidationError(message=invalid_files,
                                  code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)
        return files
