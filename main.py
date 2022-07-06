import uvicorn
from fastapi import FastAPI
from city import city_router
from sql import database

database.Base.metadata.create_all(bind=database.engine)
app = FastAPI()
app.include_router(city_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
