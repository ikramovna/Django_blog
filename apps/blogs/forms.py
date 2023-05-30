from django import forms

from .models import Comment, Contact


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
