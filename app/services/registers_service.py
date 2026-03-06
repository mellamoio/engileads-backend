from sqlalchemy.orm import Session
from app.models.registers import Registers
from app.schema.contact_schema import ContactCreate


def create_registro(db: Session, data: ContactCreate) -> Registers:
    register = Registers(
        name=data.contact_name,
        email=data.contact_email,
        phone=data.contact_phone,
        message=data.contact_message
    )

    db.add(register)
    db.commit()
    db.refresh(register)

    return register