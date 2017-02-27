import os

def get_upload_location(instance, filename):
    root, ext = os.path.splitext(filename)
    name = 'image' + ext
    return "{}/{}/{}".format(self.__class__.__name__, self.slug[:20], name)
