from fastapi import APIRouter

from crowdvibe.routes import home, users

api_router = APIRouter()
# api_router.include_router(login.router, tags=["login"])
api_router.include_router(home.router)
api_router.include_router(users.router, prefix="/users", tags=["users"])
