from django.urls import path
from blog.views import archive
urlpatterns = [
    path('', archive),
]
