from fastapi import FastAPI
from ..example_module.routes import examples

app = FastAPI()

app.include_router(examples.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}