from django.urls import path
from .views import (PurchaserListCreateView,
                    PurchaserRetrieveUpdateDestroyView, 
                    purchaserShippingDetailsListCreateView, 
                    purchaserShippingDetailRetrieveUpdateDestroyView,
                    paymentInvoiceListCreateView, 
                    paymentInvoiceRetrieveUpdateDestroyView)

urlpatterns = [
    path('purchaser/', PurchaserListCreateView.as_view()),
    path('purchaser/<pk>', PurchaserRetrieveUpdateDestroyView.as_view()),

    path('shipping/', purchaserShippingDetailsListCreateView.as_view()),
    path('shipping/<pk>', purchaserShippingDetailRetrieveUpdateDestroyView.as_view()),

    path('invoice/', paymentInvoiceListCreateView.as_view()),
    path('invoice/<pk>', paymentInvoiceRetrieveUpdateDestroyView.as_view()),
]