from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('wood/wood_list', views.wood_list, name='wood_list'),
    path('', views.index, name='index'),
    path('wood/search', views.search, name='search'),
    path('feeds/<int:pk>', views.post_detail,name='post_detail'),
    path('wood/about',views.about,name='about')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)