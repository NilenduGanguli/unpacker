from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from dbops.models.models import User, KycDocument, KycDocumentTransfer, KycDocumentExtension, SessionLocal, engine
from dbops.models.schemas import User as UserSchema, UserCreate as UserCreateSchema
from dbops.models.schemas import KycDocument as KycDocumentSchema, KycDocumentCreate as KycDocumentCreateSchema
from dbops.models.schemas import KycDocumentTransfer as KycDocumentTransferSchema, KycDocumentTransferCreate as KycDocumentTransferCreateSchema
from dbops.models.schemas import KycDocumentExtension as KycDocumentExtensionSchema, KycDocumentExtensionCreate as KycDocumentExtensionCreateSchema

app = FastAPI()

# Dependency to get a SQLAlchemy session
def get_db():
    db = SessionLocal()
    try:
        yield db  # Provide the database session to the request handler
    finally:
        db.close()  # Ensure the database session is closed after the request is handled

# User Endpoints

@app.post("/users/", response_model=UserSchema)
def create_user(user: UserCreateSchema, db: Session = Depends(get_db)):
    db_user = User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.get("/users/{soeid}", response_model=UserSchema)
def read_user(soeid: str, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.SOEID == soeid).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.put("/users/{soeid}", response_model=UserSchema)
def update_user(soeid: str, user: UserCreateSchema, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.SOEID == soeid).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    for key, value in user.model_dump().items():
        setattr(db_user, key, value)
    db.commit()
    db.refresh(db_user)
    return db_user

# KYC Document Endpoints

@app.post("/kyc_document/", response_model=KycDocumentSchema)
def create_kyc_document(kyc_document: KycDocumentCreateSchema, db: Session = Depends(get_db)):
    db_kyc_document = KycDocument(**kyc_document.model_dump())
    db.add(db_kyc_document)
    db.commit()
    db.refresh(db_kyc_document)
    return db_kyc_document

@app.get("/kyc_document/{kyc_document_id}", response_model=KycDocumentSchema)
def read_kyc_document(kyc_document_id: str, db: Session = Depends(get_db)):
    db_kyc_document = db.query(KycDocument).filter(KycDocument.KYC_DOCUMENT_ID == kyc_document_id).first()
    if db_kyc_document is None:
        raise HTTPException(status_code=404, detail="KYC Document not found")
    return db_kyc_document

@app.put("/kyc_document/{kyc_document_id}", response_model=KycDocumentSchema)
def update_kyc_document(kyc_document_id: str, kyc_document: KycDocumentCreateSchema, db: Session = Depends(get_db)):
    db_kyc_document = db.query(KycDocument).filter(KycDocument.KYC_DOCUMENT_ID == kyc_document_id).first()
    if db_kyc_document is None:
        raise HTTPException(status_code=404, detail="KYC Document not found")
    for key, value in kyc_document.model_dump().items():
        setattr(db_kyc_document, key, value)
    db.commit()
    db.refresh(db_kyc_document)
    return db_kyc_document

# KYC Document Transfer Endpoints

@app.post("/kyc_document_transfer/", response_model=KycDocumentTransferSchema)
def create_kyc_document_transfer(kyc_document_transfer: KycDocumentTransferCreateSchema, db: Session = Depends(get_db)):
    db_kyc_document_transfer = KycDocumentTransfer(**kyc_document_transfer.model_dump())
    db.add(db_kyc_document_transfer)
    db.commit()
    db.refresh(db_kyc_document_transfer)
    return db_kyc_document_transfer

@app.get("/kyc_document_transfer/{kyc_document_id}", response_model=KycDocumentTransferSchema)
def read_kyc_document_transfer(kyc_document_id: str, db: Session = Depends(get_db)):
    db_kyc_document_transfer = db.query(KycDocumentTransfer).filter(KycDocumentTransfer.KYC_DOCUMENT_ID == kyc_document_id).first()
    if db_kyc_document_transfer is None:
        raise HTTPException(status_code=404, detail="KYC Document Transfer not found")
    return db_kyc_document_transfer

@app.put("/kyc_document_transfer/{kyc_document_id}", response_model=KycDocumentTransferSchema)
def update_kyc_document_transfer(kyc_document_id: str, kyc_document_transfer: KycDocumentTransferCreateSchema, db: Session = Depends(get_db)):
    db_kyc_document_transfer = db.query(KycDocumentTransfer).filter(KycDocumentTransfer.KYC_DOCUMENT_ID == kyc_document_id).first()
    if db_kyc_document_transfer is None:
        raise HTTPException(status_code=404, detail="KYC Document Transfer not found")
    for key, value in kyc_document_transfer.model_dump().items():
        setattr(db_kyc_document_transfer, key, value)
    db.commit()
    db.refresh(db_kyc_document_transfer)
    return db_kyc_document_transfer

# KYC Document Extension Endpoints

@app.post("/kyc_document_extension/", response_model=KycDocumentExtensionSchema)
def create_kyc_document_extension(kyc_document_extension: KycDocumentExtensionCreateSchema, db: Session = Depends(get_db)):
    db_kyc_document_extension = KycDocumentExtension(**kyc_document_extension.model_dump())
    db.add(db_kyc_document_extension)
    db.commit()
    db.refresh(db_kyc_document_extension)
    return db_kyc_document_extension

@app.get("/kyc_document_extension/{kyc_document_id}", response_model=KycDocumentExtensionSchema)
def read_kyc_document_extension(kyc_document_id: str, db: Session = Depends(get_db)):
    db_kyc_document_extension = db.query(KycDocumentExtension).filter(KycDocumentExtension.KYC_DOCUMENT_ID == kyc_document_id).first()
    if db_kyc_document_extension is None:
        raise HTTPException(status_code=404, detail="KYC Document Extension not found")
    return db_kyc_document_extension

@app.put("/kyc_document_extension/{kyc_document_id}", response_model=KycDocumentExtensionSchema)
def update_kyc_document_extension(kyc_document_id: str, kyc_document_extension: KycDocumentExtensionCreateSchema, db: Session = Depends(get_db)):
    db_kyc_document_extension = db.query(KycDocumentExtension).filter(KycDocumentExtension.KYC_DOCUMENT_ID == kyc_document_id).first()
    if db_kyc_document_extension is None:
        raise HTTPException(status_code=404, detail="KYC Document Extension not found")
    for key, value in kyc_document_extension.model_dump().items():
        setattr(db_kyc_document_extension, key, value)
    db.commit()
    db.refresh(db_kyc_document_extension)
    return db_kyc_document_extension

# Startup and Shutdown events to manage database connections
# @app.on_event("startup")
# def on_startup():
#     Base.metadata.create_all(bind=engine)  # Create tables if they don't exist

# @app.on_event("shutdown")
# def on_shutdown():
#     SessionLocal().close_all()  # Close all database sessions
