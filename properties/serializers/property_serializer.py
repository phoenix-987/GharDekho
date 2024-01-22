from ..models.properties import *
from rest_framework import serializers


class PropertySerializer(serializers.ModelSerializer):

    class Meta:
        model = Properties
        fields = '__all__'

    # title = serializers.CharField(max_length=256, allow_null=False, allow_blank=False)
    # description = serializers.CharField(allow_null=False,
    #                                     allow_blank=False,
    #                                     default='Describe your property. It increases the chances to be shortlisted'
    #                                     )  # CharField(style={'base_template': 'textarea.html'})
    #
    # rental_price = serializers.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    # brokerage = serializers.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    #
    # maintenance = serializers.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    # security_deposit = serializers.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    #
    # furnishing_type = serializers.ChoiceField(allow_blank=False,choices=FURNISHING_CHOICES, default='Unfurnished')
    # carpet_area = serializers.DecimalField(max_digits=10, decimal_places=2)
    #
    # property_location = serializers.CharField(max_length=256, allow_null=False, allow_blank=False)
    # availability = serializers.ChoiceField(allow_blank=False,choices=AVAILABILITY_CHOICES, default='Immediately')
    #
    # tenant_type = serializers.ChoiceField(allow_blank=False,choices=TENANT_CHOICES, default='Any')
    # property_age = serializers.CharField(max_length=5, allow_null=False, allow_blank=False, default='New')
    #
    # property_images = PropertyImagesSerializer(many=True, read_only=True, allow_null=True, required=False)
