import asyncio
from datetime import datetime
from fastapi import FastAPI
from pydantic import BaseModel

class Alert(BaseModel):
    event_id: str
    source: str
    message: str
    timestamp: datetime

class AlertService:

    def __init__(self):
        self.alerts: list[Alert] = []
        self.lock = asyncio.Lock()

    async def add_alert(self, alert: Alert):
        await asyncio.sleep(3)

        async with self.lock:
            self.alerts.append(alert)

    async def get_alerts(self) -> list[Alert]:
        async with self.lock:
            return self.alerts.copy()

app = FastAPI()
alert_service = AlertService()

@app.post("/webhook")
async def receive_alert(alert: Alert):

    await alert_service.add_alert(alert)

    return {
        "status": "processed",
        "event_id": alert.event_id
    }

@app.get("/alerts", response_model=list[Alert])
async def get_alerts():

    return await alert_service.get_alerts()
