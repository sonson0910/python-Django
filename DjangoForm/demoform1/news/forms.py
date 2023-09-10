from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'create_time', )
        widgets = {
            'title' : forms.TextInput(attrs={'class':'tieude123'}),
            # 'content': forms.Textarea(widget = forms.Textarea(attrs={'class':'nguyenson123'})),
        }

class SendEmail(forms.Form):
    title = forms.CharField(max_length = 200, widget=forms.TextInput(attrs={'class':'tieude'}))
    content = forms.CharField(widget=forms.Textarea(attrs = {'class':'nguyenson', 'id':'noidung'}))
    email = forms.EmailField()
    cc = forms.BooleanField(required=False)