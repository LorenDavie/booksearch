""" 
Forms for Booksearch
"""

from django import forms
from booksearch.booksapi import search


class SearchForm(forms.Form):
    """ 
    Form for search.
    """

    query = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Search for Books"}
        )
    )

    def search_books(self):
        """ 
        Gets books for the specified query.
        """
        return search(self.cleaned_data["query"])
