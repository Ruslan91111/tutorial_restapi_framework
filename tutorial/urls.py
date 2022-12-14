from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from snippets.views import snippet_list, snippet_detail

router = routers.DefaultRouter()
router.register(r'snippets', snippet_list)

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', include(router.urls)),

]
