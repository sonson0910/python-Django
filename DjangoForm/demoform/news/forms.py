from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'time_create', )
        widget = {
            'title':forms.TextInput(attrs={'class':'sonnguyen'})
        }

class SendEmail(forms.Form):
    title = forms.CharField(max_length=100, widget = forms.TextInput(attrs = {'class':'tieude'}))
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea(attrs = {'class':'nguyenson'}))
    cc = forms.BooleanField(required=False)
