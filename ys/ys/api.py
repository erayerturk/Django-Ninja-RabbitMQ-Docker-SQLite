import os

from ninja import NinjaAPI

from backend.api import router as backend_router

api = NinjaAPI()

api.add_router('/', backend_router, tags=["backend"])
