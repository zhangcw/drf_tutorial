from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views_generic_cbv import SnippetList, SnippetDetail

urlpatterns = [
    path('snippets/', SnippetList.as_view()),
    path('snippet/<int:pk>/', SnippetDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)