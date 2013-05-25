from django import forms

class IdeaForm(forms.Form):
    idea_title = forms.CharField(required=True)
    idea_text = forms.CharField(required=True, widget=forms.Textarea)
    
class CommentForm(forms.Form):
    comment_text = forms.CharField(required=True, widget=forms.Textarea)
