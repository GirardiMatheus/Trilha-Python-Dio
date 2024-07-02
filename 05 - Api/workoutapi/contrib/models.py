from uuid import uuid4
from sqlalchemy import UUID 
from sqlalchemy.orm import DeclarativeBases, Mapped, mapped_column 
from sqlalchemy.dialects.postgresql import UUID as PG_UUID


class BaseModel(DeclarativeBases):
    id: Mapped[UUID] = mapped_column(PG_UUID(as_uuid=True), default=uuid4, nullable=False)
