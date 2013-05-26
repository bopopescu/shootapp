from django import forms

class IdeaForm(forms.Form):
    idea_title = forms.CharField(required=True, label='', initial='Enter idea title...')
    idea_text = forms.CharField(required=True, widget=forms.Textarea, label='', initial='Describe your idea...')
    
class CommentForm(forms.Form):
    comment_text = forms.CharField(required=True, widget=forms.Textarea, label='')
