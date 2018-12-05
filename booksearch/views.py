""" 
Views for Booksearch.
"""
from django.shortcuts import render
from booksearch.forms import SearchForm


def home(request):
    """ 
    Main index page.
    """
    form = SearchForm()
    return render(request, "home.html", {"form": form})


def search(request):
    """ 
    Search for books.
    """
    query = request.GET.get("query", "")
    form = SearchForm(request.GET)
    results = []

    if form.is_valid():
        results = form.search_books()

    result_count = len(results)

    return render(
        request,
        "search.html",
        {
            "query": query,
            "form": form,
            "results": results,
            "result_count": result_count,
        },
    )
