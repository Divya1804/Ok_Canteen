from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.db.main import init_db
from src.routes.category_routes import category_router
from src.routes.item_routes import items_router
from src.routes.user_auth_routes import auth_router


@asynccontextmanager
async def life_span(app:FastAPI):
    print("Server is started...")
    await init_db()
    yield
    print("Server is stopped...")

version = "v1"

app = FastAPI(
    title="Canteen Management System",
    description="A large scale project to phase and solve all the new deficulties.",
    version=version,
    # lifespan=life_span
)

app.include_router(auth_router, prefix=f"/api/{version}/user")
app.include_router(category_router, prefix=f"/api/{version}/category")
app.include_router(items_router, prefix=f"/api/{version}/category")
# app.include_router(book_router, prefix=f"/api/{version}/books")

# Command to run the Application...
# ------------------------------------
# fastapi dev src/main.py --port 5005