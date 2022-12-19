from django.contrib import admin
from django.urls import path, include
# from rest_framework import routers
#
# from snippets.views import snippet_list, snippet_detail
#
# router = routers.DefaultRouter()
#
# router.register(r'snippets', snippet_list, basename='list_of_snippets')
# router.register(r'snippets/<int:pk>', snippet_detail, basename='detail_snippet')


urlpatterns = [
    path('admin/', admin.site.urls),

]

# urlpatterns += router.urls