from django.db import models
from django.core.urlresolvers import reverse

from users.models import User


class CommentManager(models.Manager):

    def get_queryset(self):
        queryset = super(CommentManager, self).get_queryset()
        return queryset.select_related(
            'post',
            'user',
        )


class Comment(models.Model):

    objects = CommentManager()

    user = models.ForeignKey(
        User,
    )

    post = models.ForeignKey("Post")
    content = models.CharField(
        max_length=100,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        verbose_name = "댓글"
        verbose_name_plural = verbose_name

    def __str__(self):
        return 'Commented "{comment_content}" on "{post_title}"'.format(
            comment_content=self.content,
            post_title=self.post.title,
        )

    def get_absolute_url(self):
        return "{post_url}{comment_tag_id}".format(
            post_url = reverse(
                "post",
                kwargs={
                    "pk": self.post.id,
                }
            ),
            comment_tag_id = "#comment_{comment_id}".format(
                comment_id=self.id,
            ),
        )

    def get_object_dict(self):
        return {
            "content": self.content,
        }
