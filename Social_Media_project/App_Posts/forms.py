from django import forms
from App_Posts.models import Post


# modify model structure
class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['image', 'caption',]
        