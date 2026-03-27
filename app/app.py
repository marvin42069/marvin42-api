from fastapi import FastAPI
from .routers.auth_router import router as auth_router
#from typing import Dict, List, Optional, Sequence, Set, Tuple, Union

app = FastAPI()

#should automagically import all routes
app.include_router(auth_router)