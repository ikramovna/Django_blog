from django.contrib.auth.models import User
from django.db.models import (Model, IntegerField, CharField, SlugField, ForeignKey, CASCADE, DateTimeField, TextField,
                              BooleanField, EmailField)

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Post(Model):
    title = CharField(max_length=200, unique=True)
    slug = SlugField(max_length=200, unique=True)
    author = ForeignKey(User, on_delete=CASCADE, related_name='blog_posts')
    updated_on = DateTimeField(auto_now=True)
    content = TextField()
    created_on = DateTimeField(auto_now_add=True)
    status = IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class Comment(Model):
    post = ForeignKey(Post, on_delete=CASCADE, related_name='comments')
    name = CharField(max_length=80)
    email = EmailField()
    body = TextField()
    created_on = DateTimeField(auto_now_add=True)
    active = BooleanField(default=False)


class Contact(Model):
    message = TextField()
    name = CharField(max_length=100)
    email = EmailField()
    job_salary = TextField()
