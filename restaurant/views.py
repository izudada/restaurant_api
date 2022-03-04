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
                - serializer = stores the serialized data
    """

    #   Check if item id exists using try block
    try:
        menu_item = Menu.objects.get(id=id)
    except Menu.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    #   Save and return serialized data
    serializer = MenuSerializer(menu_item)
    return Response(serializer.data)

@api_view(['PUT',])
def api_menu_update_view(request, id):
    """
        An endpoint to update the  a menu item

        variables:
                - menu_item = stores the item gotten through url id parameter
                - serializer = stores the serialized data
                - data = a dictionary that stores response
    """

    #   Check if item id exists using try block
    try:
        menu_item = Menu.objects.get(id=id)
    except Menu.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    #   Save and return serialized data
    serializer = MenuSerializer(menu_item, data=request.data)
    data = {}

    #   Serializer checks if data sent is valid
    if serializer.is_valid():
        serializer.save()
        data["success"] = "update successful"
        return Response(data=data)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)