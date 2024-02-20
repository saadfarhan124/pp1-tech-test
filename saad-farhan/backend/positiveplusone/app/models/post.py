from sqlalchemy import Column, String, ForeignKey, Integer, Date, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database.database import Base

class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True)
    caption = Column(String)
    image_uri = Column(String)
    like_count = Column(Integer)
    # Define the many-to-one relationship with User
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='posts')
    # Define the one-to-many relationship with Tag
    tags = relationship('Tag', back_populates='post', cascade='all, delete-orphan')
     # Define the one-to-many relationship with Comments
    comments = relationship('Tag', back_populates='post', cascade='all, delete-orphan')
    time_created = Column(DateTime(timezone=True),
                          server_default=func.now(), nullable=False)
    time_updated = Column(DateTime(
        timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)