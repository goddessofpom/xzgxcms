# -*- coding: utf-8 -*- 
def decode_base64_file(data):
    '''
    ' 将base64图片转为ImageField可保存的类型
    '
    '''
  
    def get_file_extension(file_name, decode_file):
        import imghdr

        extension = imghdr.what(file_name,decode_file)
        extension = "jpg" if extension == "jpeg" else extension 

        return extension



    from django.core.files.base import ContentFile
    import base64
    import six
    import uuid

    if isinstance(data,six.string_types):
    
        if 'data:' in data and ";base64," in data:
            header, data = data.split(";base64,")

        try:
            decoded_file = base64.b64decode(data)
        except TypeError:
            TypeError('invalid_image')


        file_name = str(uuid.uuid4())[:12] 

        file_extension = get_file_extension(file_name, decoded_file)

        complete_file_name = "%s.%s" % (file_name, file_extension,)

        return ContentFile(decoded_file, name=complete_file_name)