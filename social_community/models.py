from django.db import models
from django.db.models import CASCADE

from feed.models import UserDetail
from social_community.constants import PostTypeConstant


class PostPhoto(models.Model):
    class Meta:
        db_table = "post_pictures"

    link = models.CharField(max_length=1000, null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class PostComments(models.Model):
    class Meta:
        db_table = "post_comments"

    post = models.ForeignKey('social_community.Post', null=False, on_delete=CASCADE)
    user = models.ForeignKey(UserDetail, null=False, on_delete=CASCADE)
    data = models.CharField(max_length=10000, null=False)
    created = models.DateTimeField(auto_now_add=True)
    blocked = models.BooleanField(default=False)


class PostShares(models.Model):
    class Meta:
        db_table = "post_shares"

    post = models.ForeignKey('social_community.Post', null=False, on_delete=CASCADE)
    user = models.ForeignKey(UserDetail, null=False, on_delete=CASCADE)
    data = models.CharField(max_length=10000, null=False)
    created = models.DateTimeField(auto_now_add=True)
    blocked = models.BooleanField(default=False)


class Post(models.Model):
    class Meta:
        db_table = "post"

    type = models.IntegerField(null=False, choices=PostTypeConstant)
    photos = models.ManyToManyField(PostPhoto, blank=True)
    text = models.CharField(max_length=10000)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    blocked = models.BooleanField(default=False)
