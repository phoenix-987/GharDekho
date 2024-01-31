from rest_framework import status
from properties.models import Properties
from rest_framework.views import APIView
from rest_framework.response import Response
from properties.serializers import PropertySerializer


class PropertyListView(APIView):
    """
    Class for fetching all the properties from the database and returning them.
    """
    def get(self, request):
        try:
            # Fetching all the properties.
            properties = Properties.objects.all()
            serializer = PropertySerializer(properties, many=True)

            # List to store all the properties.
            list_of_properties = list()

            # Populating the list of properties.
            for property_obj in serializer.data:
                list_of_properties.append(property_obj)

            # Checking if the list is empty or not.
            if not list_of_properties:
                return Response(
                    {'message': 'No properties found'},
                    status=status.HTTP_204_NO_CONTENT
                )

            # Returning all the properties as response.
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )

        # Sending the response if something goes wrong with the respective error in the process.
        except Exception as e:
            return Response(
                {'message': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class GetPropertyView(APIView):
    """
    Class for fetching the requested property details from the database and returning them.
    """
    def get(self, request, pk):
        try:
            try:
                # Fetching the requested property object.
                property_obj = Properties.objects.get(pk=pk)
                serializer = PropertySerializer(property_obj)

                # Sending the details sa response.
                return Response(
                    serializer.data,
                    status=status.HTTP_200_OK
                )

            # Sending the response if property not found.
            except Properties.DoesNotExist:
                return Response(
                    {'message': 'Property does not exist.'},
                    status=status.HTTP_404_NOT_FOUND
                )

        # Sending the response if something goes wrong with the respective error during the process.
        except Exception as e:
            return Response(
                {'message': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
