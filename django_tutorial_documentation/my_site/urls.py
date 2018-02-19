
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('stocks/', include('stocks.urls')),
    path('admin/', admin.site.urls)
]
