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

@api_view(['DELETE',])
def api_menu_delete_view(request, id):
    """
        An endpoint to delete a menu item

        variables:
                - menu_item = stores the item gotten through url id parameter
                - data = a dictionary that stores response
                - action = for deleting an item
    """

    #   Check if item id exists using try block
    try:
        menu_item = Menu.objects.get(id=id)
    except Menu.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    action = menu_item.delete()
    data = {}

    #   Check if action was sucessful or not
    if action:
        data["success"] = "delete successful"
    else:
        data["failure"] = "delete failed"
    return Response(data=data)

@api_view(['POST',])
def api_menu_create_view(request):
    """
        An endpoint to delete a menu item

        variables:
                - restaurant = Get Hardcoded restaurant id
                - menu_item = Using harcoded restaurant as foreign key
                - serializer = serialize request data
    """
    #   Hardcoding the restaurant for now
    restaurant = Restaurant.objects.get(pk=1)

    #   Using harcoded restaurant as foreign key
    menu_item = Menu(restaurant=restaurant)

    serializer = MenuSerializer(menu_item, data=request.data)

    #   Check if serializer is valid
    if serializer.is_valid:
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATE)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
