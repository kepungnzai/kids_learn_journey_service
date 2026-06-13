from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from database import connect_to_mongo, disconnect_from_mongo
from schema import schema

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    await connect_to_mongo()

@app.on_event("shutdown")
async def shutdown_event():
    await disconnect_from_mongo()

app.include_router(GraphQLRouter(schema))