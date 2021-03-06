from django import forms

class IdeaForm(forms.Form):
    idea_title = forms.CharField(required=True, label='', initial='Enter idea title...', max_length=100)
    idea_text = forms.CharField(required=True, widget=forms.Textarea, label='', initial='Describe your idea...', max_length=1000)
    
class CommentForm(forms.Form):
    comment_text = forms.CharField(required=True, widget=forms.Textarea, label='', max_length=1000)
