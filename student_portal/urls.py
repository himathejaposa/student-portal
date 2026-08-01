from django.views.generic import RedirectView
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('attendance/', include('attendance.urls')),
    path('courses/', include('courses.urls')),
    path('expenses/', include('expenses.urls')),
    path('notes/', include('notes.urls')),
path('', RedirectView.as_view(url='/accounts/login/', permanent=False)),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)