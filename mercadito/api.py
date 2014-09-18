from django.contrib.auth.models import User
from tastypie import fields
from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from mercadito.models import Post


class AuthorResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'author'
        excludes = ['email', 'password', 'is_active', 'is_staff', 'is_superuser']
        allowed_methods = ['get']


class PostResource(ModelResource):
    author = fields.ForeignKey(AuthorResource, 'author')

    class Meta:
        queryset = Post.objects.all()
        resource_name = 'post'
        authorization = Authorization()
