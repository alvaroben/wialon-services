from fastapi import FastAPI
from app.routers import locator_router

app = FastAPI(title="Gurtam Microservice")
app.include_router(locator_router.router)
