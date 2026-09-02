from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("my_apps.hosaik.urls")),
    path("portafolios/", include("my_apps.portafolios.urls")),
    path("accounts/", include("my_apps.accounts.urls")),
    path("tasker/", include("my_apps.tasker.urls")),
    path("mora/", include("my_apps.mora.urls")),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
