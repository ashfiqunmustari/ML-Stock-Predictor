from django.urls import path
from .views import StockPredictionAPIView

urlpatterns = [
    path('stock/', StockPredictionAPIView.as_view(), name='predict_stock'),
]

