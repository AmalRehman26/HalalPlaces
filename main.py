from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from contextlib import asynccontextmanager

from src.database import create_db_and_tables
from src.routers import restaurants, reviews, fragments, pages

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Create database tables
    create_db_and_tables()
    yield
    # Shutdown: cleanup if needed

app = FastAPI(
    title="Halal Restaurant Review API",
    description="A full-stack restaurant review application",
    version="1.0.0",
    lifespan=lifespan
)

# Include routers
app.include_router(restaurants.router)
app.include_router(reviews.router)
app.include_router(fragments.router)
app.include_router(pages.router)

# Mount static files
# app.mount("/static", StaticFiles(directory="static"), name="static")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)