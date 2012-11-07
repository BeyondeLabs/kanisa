from django import forms
from kanisa.forms import KanisaBaseForm
from kanisa.models import Service, Song


class AddSongToServiceForm(KanisaBaseForm):
    song = forms.ModelChoiceField(queryset=Song.objects.all())
    submit_text = 'Add Song'
