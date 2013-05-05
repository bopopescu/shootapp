from django import forms

class IdeaForm(forms.Form):
    idea_title = forms.CharField()
    idea_text = forms.CharField()