from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter

from movies.views import MovieViewSet

router = SimpleRouter()
router.register(r'movie', MovieViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),

]

urlpatterns += router.urls


