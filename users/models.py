import os
from io import BytesIO
from django.contrib import admin
from django.contrib.auth.models import AbstractUser
from django.core.files.base import ContentFile
from django.db import models
from PIL import Image, ImageChops


def content_file_name(instance, filename):
    filename = f"{instance.username}_avatar{os.path.splitext(filename)[1]}"
    return '/'.join(['avatars', 'originals',filename])


class User(AbstractUser):
    middle_name = models.CharField(max_length=50, blank=True)
    avatar_url = models.ImageField(upload_to=content_file_name, null=True, blank=True)
    thumbnail = models.ImageField(upload_to=f'avatars/thumbnail/', null=True, blank=True)
    __original_mode = None

    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)
        self.__original_mode = self.avatar_url

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        if self.avatar_url != self.__original_mode:
            self.__original_mode = self.avatar_url
            self.get_avatar()
        super(User, self).save(force_insert, force_update, *args, **kwargs)

    def get_avatar(self):
        if not self.avatar_url:
            return
        image = Image.open(self.avatar_url)
        image.thumbnail((50, 50), Image.ANTIALIAS)
        thumb_name, thumb_extension = os.path.splitext(self.avatar_url.name)
        thumb_filename = thumb_name + '_thumb' + thumb_extension

        if thumb_extension in ['.jpg', '.jpeg']:
            FTYPE = 'JPEG'
        elif thumb_extension == '.png':
            FTYPE = 'PNG'
        else:
            return False

        temp_thumb = BytesIO()
        image.save(temp_thumb, FTYPE)
        temp_thumb.seek(0)

        self.thumbnail.save(thumb_filename, ContentFile(temp_thumb.read()), save=True)
        temp_thumb.close()
        return True


class CourseAssignStudent(models.Model):
    course = models.ForeignKey('course.Course', on_delete=models.CASCADE, null=False)
    user = models.ForeignKey(User, related_name='assigns', on_delete=models.CASCADE, null=False)


class CourseAssignTeacher(models.Model):
    course = models.ForeignKey('course.Course', on_delete=models.CASCADE, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)


admin.site.register(User)
