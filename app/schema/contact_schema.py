from pydantic import BaseModel, EmailStr

class ContactCreate(BaseModel):
    contact_name: str
    contact_email: EmailStr
    contact_phone: str
    contact_message: str

class ContactData(BaseModel):
    id: int


class ContactResponse(BaseModel):
    success: bool
    message: str
    data: ContactData