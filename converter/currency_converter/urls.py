from django.urls import path
from .views import CurrencyconverterAPIview

urlpatterns = [

    path("convert/",CurrencyconverterAPIview.as_view(),name='currency_convert_api')
    
]