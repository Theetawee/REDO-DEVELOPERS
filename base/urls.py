from django.contrib import admin
from django.urls import include, path, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from base.sitemaps import StaticViewSitemap, ProfileSitemap
from django.views.generic.base import TemplateView
from base.utils import service_worker, manifest, offline
from django.conf.urls.i18n import i18n_patterns

sitemaps = {"others": StaticViewSitemap, "profiles": ProfileSitemap}


urlpatterns = [
    re_path(r"^serviceworker\.js$", service_worker, name="sw"),
    re_path(r"^manifest\.json$", manifest, name="manifest"),
    path("offline/", offline, name="offline"),
    path(
        "robots.txt",
        TemplateView.as_view(
            template_name="base/robots.txt", content_type="text/plain"
        ),
        name="robots",
    ),
    # path("", include("main.urls")),
    # path("accounts/", include("accounts.urls")),
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
    path("i18n/", include("django.conf.urls.i18n")),
    path("admin/", admin.site.urls),
]

urlpatterns += i18n_patterns(
    path("", include("main.urls")),
    path("accounts/", include("accounts.urls")),
    prefix_default_language=True,
)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += (path("__debug__/", include(debug_toolbar.urls)),)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


handler404 = "base.utils.custom_404_view"
handler400 = "base.utils.custom_404_view"
handler500 = "base.utils.custom_500_view"
handler403 = "base.utils.custom_404_view"

admin.site.site_header = "App name"
admin.site.site_title = "App Admin"
admin.site.index_title = "Welcome to the Admin Panel"
