from sqlalchemy import UUID 
from sqlalchemy.orm import DeclarativeBases, Mapped 

class BaseModel(DeclarativeBases):
    id: Mapped[UUID] = mapped_co