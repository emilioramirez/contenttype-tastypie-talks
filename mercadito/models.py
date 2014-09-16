from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType


class Tag(models.Model):
    tag_name = models.CharField(max_length=100)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __unicode__(self):
        return self.tag_name


class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, related_name="posts")
    created = models.DateTimeField(auto_now_add=True)
    tags = GenericRelation(Tag, related_query_name='posts')

    def __unicode__(self):
        return self.title


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __unicode__(self):
        return self.name


class Picture(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(blank=True)

    def __unicode__(self):
        return self.name
