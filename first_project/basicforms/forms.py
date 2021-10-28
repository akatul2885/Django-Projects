from django import forms

class CommentForm(forms.Form):
    name = forms.CharField(max_length=50, required=True, label='Name')
    email = forms.EmailField(required=True, label='Email')
    text = forms.CharField(widget=forms.Textarea, label='Comment')
