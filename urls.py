from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('otu-table/', views.otu_table_view, name='otu_table'),
]
from django.urls import path, include

urlpatterns = [
    path('otu-table/', include('otu_table_app.urls')),
]

urlpatterns = [
    # ... your other URL patterns ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
