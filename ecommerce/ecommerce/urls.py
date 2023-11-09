from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    # todo Admin url

    path('admin/', admin.site.urls),

    # todo Store app

    path('', include('store.urls')),

    # todo Cart app

    path('cart/', include('cart.urls')),

    # todo Account app

    path('account/', include('account.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
