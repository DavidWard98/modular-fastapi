from fastapi import FastAPI
from app.modules.example_module.routes import examples
from .core.routing import GraphQLRouter
import strawberry


app = FastAPI()
app.include_router(examples.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}