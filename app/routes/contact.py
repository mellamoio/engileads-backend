from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.schema.contact_schema import ContactCreate, ContactResponse, ContactData
from app.services.registers_service import create_registro
from app.dependencies import get_db

router = APIRouter(
    prefix="/contact",
    tags=["Contact"]
)


@router.post(
    "/",
    response_model=ContactResponse,
    status_code=status.HTTP_201_CREATED
)
def create_contact(
    data: ContactCreate,
    db: Session = Depends(get_db)
):
    registro = create_registro(db, data)

    return ContactResponse(
        success=True,
        message="Registro creado correctamente",
        data=ContactData(id=registro.id)
    )