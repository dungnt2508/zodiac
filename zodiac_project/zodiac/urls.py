from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import reverse_lazy


app_name = 'zodiac'
urlpatterns = [
    path('12-con-giap/', views.zodiac_info, name='info'),
    path('du-doan/', views.zodiac_predict, name='predict'),
    path("latest_lucky_zodiac/", views.latest_lucky_zodiac, name="latest_lucky_zodiac"),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
