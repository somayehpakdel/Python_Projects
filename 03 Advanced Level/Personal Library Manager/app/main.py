from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import configuration
from app.config import settings
from app.core.errors import setup_exception_handlers


# Import the routers
from app.api.v1 import books as books_api
from app.api.v1 import users as users_api


app = FastAPI(title=settings.APP_TITLE, version=settings.APP_VERSION)
setup_exception_handlers(app)
# --- CORS Middleware Configuration ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"], 
)

# --- Include Routers ---
# We include the routers with versioning prefixes
app.include_router(
    books_api.router, 
    prefix="/api/v1/books", 
    tags=["Books"]
)

app.include_router(
    users_api.router, 
    prefix="/api/v1/users", 
    tags=["Users"]
)

# --- Root Endpoint ---
@app.get("/")
def read_root():
    return {"message": "Welcome to the Personal Library API", "docs": "/docs"}