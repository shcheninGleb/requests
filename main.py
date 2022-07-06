from fastapi import FastAPI

from sql import database
from sql import api

if __name__ == '__main__':

database.Base.metadata.create_all(bind=database.engine)

app = FastAPI()
# хз что тут делать, вроде надо прописать рут, но я хз как
app.include_router(api.router)
