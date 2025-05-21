from pydantic import BaseModel
from datetime import datetime

class Transaction(BaseModel):
    id: str
    amount: float
    timestamp: datetime
    merchant: str
    card_number: str
    location: str