from django import forms

from blog.models import Post


class PostForm(forms.ModelForm):
    """docstring for PostForm"""
    class Meta:
        model = Post
        fields = ('title', 'text',)
