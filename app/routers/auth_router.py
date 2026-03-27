from fastapi import APIRouter,Depends,HTTPException

router = APIRouter()

@router.get('/hello')
def hello():
    """Dummy route"""
    return "hello mirko from route"