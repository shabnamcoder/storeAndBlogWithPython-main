from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from azbankgateways.urls import az_bank_gateways_urls
from order.views import go_to_gateway_view

urlpatterns = [
   path('admin/', admin.site.urls),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken')),
    path('api/v1/', include('product.urls')),
    path('api/v1/', include('blog.urls')),
    path('bankgateways/', az_bank_gateways_urls()),
    path('go_to_gateway/',go_to_gateway_view),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
