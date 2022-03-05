from django.urls import path

from .views import (
    api_menu_detail_view, 
    api_menu_update_view,
    api_menu_delete_view,
    api_menu_create_view,
)


urlpatterns = [
    path('<int:id>/', api_menu_detail_view, name="menu_detail"),
]