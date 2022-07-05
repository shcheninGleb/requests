from fastapi import FastAPI

from sql import database
from sql import main


if __name__ == '__main__':
database.Base.metadata.create_all(bind=database.engine)

app = FastAPI()
app.include_router(main.router) #хз что тут делать
