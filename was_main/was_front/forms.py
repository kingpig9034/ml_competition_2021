from was_rest.models import Score
from django import forms

class ScoreForm(forms.ModelForm):
    class Meta:
        model = Score
        fields = ('file', 'user_id')