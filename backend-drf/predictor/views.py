from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error, r2_score
from keras.models import load_model

class StockPredictionAPIView(APIView):
    def post(self, request):
        ticker = request.data.get('ticker')
        if not ticker:
            return Response({"error": "Ticker is required"}, status=status.HTTP_400_BAD_REQUEST)

        df = yf.download(ticker, period='5y')
        if df.empty:
            return Response({"error": "No data found for the given ticker."}, status=status.HTTP_404_NOT_FOUND)

        df = df.reset_index()
        df_close = pd.DataFrame(df['Close'])


        data_training = df_close[:int(len(df_close)*0.7)]
        data_testing = df_close[int(len(df_close)*0.7):]

        scaler = MinMaxScaler(feature_range=(0,1))
        scaler.fit(data_training)

        past_100_days = data_training.tail(100)
        final_df = pd.concat([past_100_days, data_testing], ignore_index=True)
        input_data = scaler.transform(final_df)

        x_test = []
        for i in range(100, input_data.shape[0]):
            x_test.append(input_data[i-100:i])
        x_test = np.array(x_test)

        y_test = data_testing.values.flatten()

        model = load_model('ml-models/stock_prediction_model.keras')

        y_pred_scaled = model.predict(x_test)
        y_pred = scaler.inverse_transform(y_pred_scaled).flatten()

        mse = mean_squared_error(y_test, y_pred)
        rmse = np.sqrt(mse)
        r2 = r2_score(y_test, y_pred)

        return Response({
            "status": "success",
            "mse": mse,
            "rmse": rmse,
            "r2": r2,
            "y_test": y_test.tolist(),
            "y_predicted": y_pred.tolist()
        })
