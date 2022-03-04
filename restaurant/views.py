from itsdangerous import serializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Menu, Restaurant
from .serializers import MenuSerializer


@api_view(['GET',])
def api_menu_detail_view(request, id):
    """
        An endpoint to get the detail of a menu item

        variables:
                - menu_item = stores the item gotten through url id parameter
                - serializer = stors the serialized data
    """

    #   Check if item id exists using try block
    try:
        menu_item = Menu.objects.get(id=id)
    except Menu.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    #   Save and return serialized data
    serializer = MenuSerializer(menu_item)
    return Response(serializer.data)