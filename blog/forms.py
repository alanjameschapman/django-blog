from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """
    A form for users to submit a comment on a blog post.
    """
    class Meta:
        model = Comment
        fields = ('body',)
