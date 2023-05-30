from django.contrib.auth.models import User
from django.db.models import (Model, IntegerField, CharField, SlugField, ForeignKey, CASCADE, DateTimeField, TextField,
                              BooleanField, EmailField)

from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Post(TranslatableModel):
    translations = TranslatedFields(
        title=CharField(max_length=200, unique=True),
        slug=SlugField(max_length=200, unique=True),
        content=TextField()

    )

    author = ForeignKey(User, on_delete=CASCADE, related_name='blog_posts')
    updated_on = DateTimeField(auto_now=True)
    created_on = DateTimeField(auto_now_add=True)
    status = IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']


# class Post(Model):
#     title = CharField(_('title'), max_length=200, unique=True),
#     slug = SlugField(_('slug'), max_length=200, unique=True),
#     content = TextField(_('content'))
#     author = ForeignKey(User, on_delete=CASCADE, related_name='blog_posts')
#     updated_on = DateTimeField(auto_now=True)
#     created_on = DateTimeField(auto_now_add=True)
#     status = IntegerField(choices=STATUS, default=0)
#
#     class Meta:
#         ordering = ['-created_on']


class Comment(Model):
    body = TextField()
    post = ForeignKey('Post', on_delete=CASCADE, related_name='comments')
    name = CharField(max_length=80)
    email = EmailField()
    created_on = DateTimeField(auto_now_add=True)
    active = BooleanField(default=False)


class Contact(TranslatableModel):
    translations = TranslatedFields(
        message=TextField(),

    )
    name = CharField(max_length=100)
    email = EmailField()
    job_salary = TextField()
