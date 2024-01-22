from ..models import Properties
from rest_framework.response import Response
from rest_framework import status, serializers
from rest_framework.decorators import api_view
from ..serializers.property_serializer import PropertySerializer


@api_view(['POST'])
def add_new_property(request):
    data = request.data
    serializer = PropertySerializer(data=data)

    try:
        if serializer.is_valid():
            serializer.save()
        else:
            raise serializers.ValidationError(serializer.errors)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_206_PARTIAL_CONTENT)
        # print(e)

    return Response({'message': 'Property Added successfully'}, status=status.HTTP_201_CREATED)
