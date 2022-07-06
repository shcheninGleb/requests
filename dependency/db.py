from sql.database import SessionLocal


def getDb():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
