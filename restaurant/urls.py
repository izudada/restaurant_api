from django.urls import path

from .views import api_menu_detail_view


urlpatterns = [
    path('<int: id>/', api_menu_detail_view, name="menu_detail"),
]