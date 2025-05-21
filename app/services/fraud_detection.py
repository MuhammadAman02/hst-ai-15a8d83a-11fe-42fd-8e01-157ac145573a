import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from app.models.transaction import Transaction

class FraudDetectionService:
    def __init__(self):
        self.model = IsolationForest(contamination=0.1, random_state=42)
        self.transactions = []

    def add_transaction(self, transaction: Transaction):
        self.transactions.append(transaction)

    def train_model(self):
        if len(self.transactions) < 100:
            return "Not enough data to train the model"
        
        df = pd.DataFrame([t.dict() for t in self.transactions])
        features = ['amount', 'hour', 'day_of_week']
        df['hour'] = pd.to_datetime(df['timestamp']).dt.hour
        df['day_of_week'] = pd.to_datetime(df['timestamp']).dt.dayofweek
        
        X = df[features]
        self.model.fit(X)
        return "Model trained successfully"

    def detect_fraud(self, transaction: Transaction) -> bool:
        # Simple rule-based detection
        if transaction.amount > 10000:
            return True
        
        # Machine learning-based detection
        if len(self.transactions) >= 100:
            df = pd.DataFrame([transaction.dict()])
            df['hour'] = pd.to_datetime(df['timestamp']).dt.hour
            df['day_of_week'] = pd.to_datetime(df['timestamp']).dt.dayofweek
            X = df[['amount', 'hour', 'day_of_week']]
            prediction = self.model.predict(X)
            return prediction[0] == -1  # -1 indicates an anomaly (potential fraud)
        
        return False

fraud_detection_service = FraudDetectionService()