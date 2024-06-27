from django.contrib import admin
from django.urls import path

from azbankgateways.urls import az_bank_gateways_urls

admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bankgateways/', az_bank_gateways_urls()),
]