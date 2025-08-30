from django.contrib import admin
from django.urls import path, include  # Додайте include до імпорту
from django.conf import settings
import blango_auth.views
import blog.views

print(f"Time zone: {settings.TIME_ZONE}")

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", blog.views.index),
    path("post/<slug>/", blog.views.post_detail, name="blog-post-detail"),  # ← Додано кому тут
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/profile/", blango_auth.views.profile, name="profile"),
]