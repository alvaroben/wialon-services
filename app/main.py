from fastapi import FastAPI
from app.routers import locator_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Wialon Microservice")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(locator_router.router)
