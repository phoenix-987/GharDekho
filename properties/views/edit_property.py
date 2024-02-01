from rest_framework import status
from properties.models import Properties
from rest_framework.views import APIView
from rest_framework.response import Response
from properties.serializers import PropertySerializer
from properties.renderers import PropertiesJSONRenderer
from authorization.authentication import OwnerIsAuthenticated


class EditPropertyView(APIView):

    # Renders the output in the Json format.
    renderer_classes = [PropertiesJSONRenderer]
    # Authenticates whether the user is authorized or not to perform the action.
    permission_classes = [OwnerIsAuthenticated]

    def put(self, request, pk):
        try:
            # Fetching property details of the given id
            data = self.get_property_details(pk=pk)
            data.pop('id')
            data.pop('user')

            # Check if the passed data is whether empty or same as stored in the database.
            if request.data is None or request.data == {} or request.data == data:
                return Response(
                    {'message': 'No changes found.'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            try:
                # Making changes in the properties data.
                for key, value in request.data.items():
                    if key == 'id' or key == 'user':
                        raise Exception('Invalid property attributes.')
                    data[key] = value

                # Committing updates in the database with appropriate response.
                Properties.objects.filter(pk=pk).update(**data)
                return Response(
                    {'message': 'Property updated successfully.'},
                    status=status.HTTP_200_OK
                )

            # Sending the response if something goes wrong with the respective error while committing changes.
            except Exception as e:
                return Response(
                    {'message': str(e)},
                    status=status.HTTP_400_BAD_REQUEST
                )

        # Sending the response if something goes wrong with the respective error during update.
        except Exception as e:
            return Response(
                {'message': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    @staticmethod
    def get_property_details(pk):
        """
        Method to fetch and return the requested properties from the database.
        """
        try:
            property_obj = Properties.objects.get(pk=pk)
            serializer = PropertySerializer(property_obj)
            return dict(serializer.data)

        except Exception as e:
            raise Exception(str(e))
