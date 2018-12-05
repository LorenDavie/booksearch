""" 
Encapsulates access to the Google Books API.
"""
from apiclient.discovery import build
from django.conf import settings

service = build("books", "v1", developerKey=settings.GOOGLE_API_KEY)


def search(query):
    """ 
    Searches for books.
    """
    request = service.volumes().list(source="public", q=query)
    response = request.execute()
    return response.get("items", [])
