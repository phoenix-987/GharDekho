# import json
from ..models import Properties
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..serializers.property_serializer import PropertySerializer


@api_view(['GET'])
def list_all_properties(request):
    try:
        objects = Properties.objects.all()
        objects = PropertySerializer(objects, many=True).data
        list_of_dict = list()
        for obj in objects:
            list_of_dict.append(dict(obj))

        if not list_of_dict:
            data = {'message': 'No property found'}
            data_status = status.HTTP_204_NO_CONTENT
        else:
            data = list_of_dict
            data_status = status.HTTP_200_OK

        return Response(data, status=data_status)

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def list_properties(request, pk):
    try:
        try:
            obj = Properties.objects.get(pk=pk)
            data = {key: item for key, item in obj.__dict__.items() if key != '_state'}
            data_status = status.HTTP_200_OK

        except Properties.DoesNotExist:
            data = {'error': 'Property not found'}
            data_status = status.HTTP_204_NO_CONTENT

    except Exception as e:
        data = str(e)
        data_status = status.HTTP_500_INTERNAL_SERVER_ERROR

    return Response(data, status=data_status)
