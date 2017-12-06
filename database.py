from sqlalchemy import Column, Integer, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func

Base = declarative_base()


class Token(Base):
    __tablename__ = 'token'
    id = Column(Integer, primary_key=True)
    key = Column(Text, nullable=False)
    branch = Column(Text, nullable=False)
    original = Column(Text, nullable=False)
    translation = Column(Text, nullable=False)
    date = Column(DateTime(timezone=True), server_default=func.now())


class Database(object):
    def __init__(self):
        engine = create_engine('sqlite:///database.db')
        Base.metadata.bind = engine
        DBSession = sessionmaker(bind=engine)
        self.session = DBSession()

    def create(self):
        engine = create_engine('sqlite:///database.db')
        Base.metadata.create_all(engine)

    def add_token(self, key, branch, original, translation):
        new_token = Token(
            key=key,
            branch=branch,
            original=original,
            translation=translation
        )
        self.session.add(new_token)

    def commit(self):
        self.session.commit()

    def get_token(self, _id):
        return self.session.query(Token).filter_by(id=_id).one()

    def get_tokens(self):
        return self.session.query(Token).all()
