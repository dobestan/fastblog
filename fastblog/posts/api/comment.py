from django.views.generic import View
from django.http import HttpResponse

import json

from posts.models import Post


class PostCommentListAPIView(View):

    def get(self, request, **kwargs):
        post = Post.objects.get(pk=kwargs.get('pk'))

        data = [
            comment.get_object_dict()
            for comment
            in post.comment_set.all()
        ]

        return HttpResponse(
            json.dumps(data),
            content_type="application/json",
        )