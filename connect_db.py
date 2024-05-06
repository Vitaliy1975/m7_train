from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql://postgres:123@localhost:5432/postgres")
Session = sessionmaker(bind=engine)
session = Session()
