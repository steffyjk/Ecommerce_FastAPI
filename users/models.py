from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class Role(Base):
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    users = relationship('User', back_populates='roles')

    def __repr__(self):
        return f"<Role: {self.role}>"


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    email = Column(String, unique=True, index=True)
    password = Column(String)
    role_id = Column(Integer, ForeignKey('roles.id'))
    roles = relationship('Roles', back_populates='users')

    def __repr__(self):
        return f"<User: {self.email}>"
