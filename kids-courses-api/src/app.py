from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from .database import connect_to_mongo, disconnect_from_mongo
from .schema import schema

app = FastAPI(title="Kids Courses API")

graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/graphql")

@app.on_event("startup")
async def startup_event():
    await connect_to_mongo()

@app.on_event("shutdown")
async def shutdown_event():
    await disconnect_from_mongo()

@app.get("/")
async def health_check():
    return {"status": "ok", "message": "Kids Courses GraphQL API is running"}
