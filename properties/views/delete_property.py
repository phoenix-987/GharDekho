from ..models import Properties
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['DELETE'])
def delete_property(request, pk):
    try:
        result = Properties.objects.filter(pk=pk).delete()
        if result[0] == 1:
            data = {'msg': 'Property removed successfully'}
            data_status = status.HTTP_202_ACCEPTED
        else:
            data = {'msg': 'Property not found!'}
            data_status = status.HTTP_204_NO_CONTENT
    except Exception as e:
        data = str(e)
        data_status = status.HTTP_500_INTERNAL_SERVER_ERROR

    return Response(data, status=data_status)
