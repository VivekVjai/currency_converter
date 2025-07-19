from rest_framework import serializers

class Currencyconverterserializer(serializers.Serializer):

    amount=serializers.FloatField(min_value=0.0)
    from_currency=serializers.CharField(max_length=3)
    to_currency=serializers.CharField(max_length=3)