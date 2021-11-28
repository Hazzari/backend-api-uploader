import imghdr


def validate_img(file):
    """ Проверка размера файла и расширения
    """
    allowed_image_formats = ['jpeg', 'png', ]
    if not imghdr.what(file) in allowed_image_formats:
        return False, 'Incorrect file format'
    if file.size >= 204800:
        return False, 'Exceeding max size'
    return True, 'ok', 'Success'


def get_path_upload_image(file) -> str:
    """Построение пути к файлу изображения,
       format: (media)/image/photo.jpg
    """
    return f'./media/image/{file}'


def save_file(file):
    with open(get_path_upload_image(file.name), "wb") as f:
        for chunk in file:
            f.write(chunk)
