import uvicorn
from fastapi import FastAPI
from nicegui import ui
from app.api.routes import router as api_router
from app.frontend.ui import create_ui

app = FastAPI()
app.include_router(api_router)

create_ui()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)