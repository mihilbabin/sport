import os

def get_upload_location(instance, filename):
    root, ext = os.path.splitext(filename)
    name = 'image' + ext
    return "{}/{}/{}".format(instance.__class__.__name__, instance.slug[:20], name)
