from sqlalchemy import Column, Integer, String, Text, TIMESTAMP, func
from app.db.base import Base

class Registers(Base):
    __tablename__ = "registers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150), nullable=False)
    email = Column(String(150), nullable=False)
    phone = Column(String(50))
    message = Column(Text, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())