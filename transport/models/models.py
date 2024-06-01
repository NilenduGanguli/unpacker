from pydantic import BaseModel
from datetime import date
from typing import Optional

# Pydantic model for User base data (shared properties)
class UserBase(BaseModel):
    ENTITLEMENT_CATEGORY: str
    ENTITLEMENT_LEVEL: str

# Pydantic model for creating a User (extends UserBase)
class UserCreate(UserBase):
    SOEID: str

# Pydantic model for reading a User (extends UserBase)
class User(UserBase):
    SOEID: str

    class Config:
        orm_mode = True  # This configures Pydantic to work with SQLAlchemy models

# Pydantic model for KycDocument base data (shared properties)
class KycDocumentBase(BaseModel):
    DOCUMENT_COMPONENT_STATE: str
    DOCUMENT_LINK_ID: str
    DOCUMENT_TYPE: str
    DOCUMENT_SUB_TYPE: Optional[str]
    DOCUMENT_NAME: str
    DOCUMENT_LOCATION: Optional[str]
    CREATE_ID: Optional[str]
    CREATE_DT: date

# Pydantic model for creating a KycDocument (extends KycDocumentBase)
class KycDocumentCreate(KycDocumentBase):
    KYC_DOCUMENT_ID: str

# Pydantic model for reading a KycDocument (extends KycDocumentBase)
class KycDocument(KycDocumentBase):
    KYC_DOCUMENT_ID: str

    class Config:
        orm_mode = True  # This configures Pydantic to work with SQLAlchemy models

# Pydantic model for KycDocumentTransfer base data (shared properties)
class KycDocumentTransferBase(BaseModel):
    DOCUMENT_COMPONENT_STATE: str
    DOCUMENT_LINK_ID: str
    DOCUMENT_NAME: str
    DOCUMENT_S3_LOCATION: Optional[str]
    BATCH_ID: str
    BATCH_DT: date
    CREATE_ID: Optional[str]
    CREATE_DT: date

# Pydantic model for creating a KycDocumentTransfer (extends KycDocumentTransferBase)
class KycDocumentTransferCreate(KycDocumentTransferBase):
    KYC_DOCUMENT_ID: str

# Pydantic model for reading a KycDocumentTransfer (extends KycDocumentTransferBase)
class KycDocumentTransfer(KycDocumentTransferBase):
    KYC_DOCUMENT_ID: str

    class Config:
        orm_mode = True  # This configures Pydantic to work with SQLAlchemy models

# Pydantic model for KycDocumentExtension base data (shared properties)
class KycDocumentExtensionBase(BaseModel):
    DOCUMENT_COMPONENT_STATE: str
    KYC_DOCUMENT_EXTENSION_ID: Optional[str]
    DOCUMENT_LINK_ID: str
    DOCUMENT_TYPE: str
    DOCUMENT_SUB_TYPE: Optional[str]
    DOCUMENT_NAME: str
    DOCUMENT_S3_LOCATION: Optional[str]
    INNER_DOCUMENT_ID: Optional[str]
    INNER_DOCUMENT: Optional[str]
    BATCH_ID: str
    BATCH_DT: date
    CREATE_ID: Optional[str]
    CREATE_DT: date

# Pydantic model for creating a KycDocumentExtension (extends KycDocumentExtensionBase)
class KycDocumentExtensionCreate(KycDocumentExtensionBase):
    KYC_DOCUMENT_ID: str

# Pydantic model for reading a KycDocumentExtension (extends KycDocumentExtensionBase)
class KycDocumentExtension(KycDocumentExtensionBase):
    KYC_DOCUMENT_ID: str

    class Config:
        orm_mode = True  # This configures Pydantic to work with SQLAlchemy models
