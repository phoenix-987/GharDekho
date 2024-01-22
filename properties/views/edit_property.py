from ..models import Properties
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..serializers.property_serializer import PropertySerializer


@api_view(['PUT'])
def edit_property(request, pk):
    def get_property_details(property_id):
        try:
            property_detail = Properties.objects.get(pk=property_id)
            serializer = PropertySerializer(property_detail)
            return {'msg': dict(serializer.data)}, status.HTTP_200_OK
        except Exception as e:
            return {'error': str(e)}, status.HTTP_400_BAD_REQUEST

    try:
        data, data_status = get_property_details(pk)
        data = data['msg']

        if data_status == 200:
            for key, value in request.data.items():
                data[key] = value

            Properties.objects.filter(pk=pk).update(**data)
            data, data_status = get_property_details(pk)
            data = data['msg']
            data_status = status.HTTP_202_ACCEPTED

        else:
            raise Exception(data)

    except Exception as e:
        data = {'error': str(e)}
        data_status = status.HTTP_400_BAD_REQUEST

    return Response(data, status=data_status)
