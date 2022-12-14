from django.urls import path
from .views import snippet_list, snippet_detail


urlpatterns = [
    path(r'snippets/', snippet_list),
    path(r'snippets/(?P<pk>[0-9]+)/', snippet_detail),
]

snippet_detail
