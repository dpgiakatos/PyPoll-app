from fastapi import APIRouter
from app.auth import auth
from app.user import user
from app.graph import graph


router = APIRouter()
router.include_router(auth.router)
router.include_router(user.router)
router.include_router(graph.router)
