
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
from .serializers import Currencyconverterserializer
import os

class CurrencyconverterAPIview(APIView):
    def post(self, request):
        serializer = Currencyconverterserializer(data=request.data)

        if serializer.is_valid():
            amount = serializer.validated_data['amount']
            from_curr = serializer.validated_data['from_currency'].upper()
            to_curr = serializer.validated_data['to_currency'].upper()

            
            ACCESS_KEY = os.getenv('API_KEY')

            api_url = (
                f"https://api.apilayer.com/exchangerates_data/convert"
                f"?from={from_curr}&to={to_curr}&amount={amount}"
            )

            headers = {
                "apikey": ACCESS_KEY
            }

            try:
                api_response = requests.get(api_url, headers=headers)
                data = api_response.json()

                print("API response:", data) 

                if data.get("success") and "result" in data and "info" in data and "rate" in data["info"]:
                    rate = data["info"]["rate"]
                    converted = data["result"]

                    return Response({
                        "amount": amount,
                        "from_currency": from_curr,
                        "to_currency": to_curr,
                        "rate": rate,
                        "converted_amount": round(converted, 2)
                    })

                return Response(
                    {"error": "Invalid currency code or data missing."},
                    status=status.HTTP_400_BAD_REQUEST
                )

            except Exception as e:
                return Response(
                    {"error": f"API request failed: {str(e)}"},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
