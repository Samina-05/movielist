from django import forms

class MovieForm(forms.Form):
    movie_name = forms.CharField(label='Name', max_length=50)
    