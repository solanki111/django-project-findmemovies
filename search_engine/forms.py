from django import forms


class LatestForm(forms.ModelForm):
    class Meta:
        # model = MoviesDB
        fields = [
            'db_title',
            'url'
        ]


class SimilarForm(forms.Form):
    Title = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Search a movie..'
        }
    ))
    # pages = forms.IntegerField(required=False, placeholer='optional')


class DiscoverForm(forms.Form):
    title = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Search a movie..'
        }
    ))
    # pages = forms.IntegerField(required=False, placeholer='optional')
