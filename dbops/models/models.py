from sqlalchemy import Column, String, Date, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the database URL
DATABASE_URL = "postgresql://user:password@localhost/dbname"

# Create the SQLAlchemy engine to connect to the database
engine = create_engine(DATABASE_URL)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for our class definitions
Base = declarative_base()

# Define the User model which maps to the 'users' table
class User(Base):
    __tablename__ = "users"
    
    SOEID = Column(String(7), primary_key=True, index=True)
    ENTITLEMENT_CATEGORY = Column(String(50), nullable=False)
    ENTITLEMENT_LEVEL = Column(String(50), nullable=False)

# Define the KycDocument model which maps to the 'KYC_DOCUMENT' table
class KycDocument(Base):
    __tablename__ = "KYC_DOCUMENT"
    
    KYC_DOCUMENT_ID = Column(String(50), primary_key=True, index=True)
    DOCUMENT_COMPONENT_STATE = Column(String(50), nullable=False)
    DOCUMENT_LINK_ID = Column(String(50), nullable=False)
    DOCUMENT_TYPE = Column(String(50), nullable=False)
    DOCUMENT_SUB_TYPE = Column(String(50))
    DOCUMENT_NAME = Column(String(255), nullable=False)
    DOCUMENT_LOCATION = Column(String(255))
    CREATE_ID = Column(String(50))
    CREATE_DT = Column(Date, nullable=False)

# Define the KycDocumentTransfer model which maps to the 'KYC_DOCUMENT_TRANSFER' table
class KycDocumentTransfer(Base):
    __tablename__ = "KYC_DOCUMENT_TRANSFER"
    
    KYC_DOCUMENT_ID = Column(String(50), primary_key=True, index=True)
    DOCUMENT_COMPONENT_STATE = Column(String(50), nullable=False)
    DOCUMENT_LINK_ID = Column(String(50), nullable=False)
    DOCUMENT_NAME = Column(String(255), nullable=False)
    DOCUMENT_S3_LOCATION = Column(String(255))
    BATCH_ID = Column(String(50), nullable=False)
    BATCH_DT = Column(Date, nullable=False)
    CREATE_ID = Column(String(50))
    CREATE_DT = Column(Date, nullable=False)

# Define the KycDocumentExtension model which maps to the 'KYC_DOCUMENT_EXTENSION' table
class KycDocumentExtension(Base):
    __tablename__ = "KYC_DOCUMENT_EXTENSION"
    
    KYC_DOCUMENT_ID = Column(String(50), primary_key=True, index=True)
    DOCUMENT_COMPONENT_STATE = Column(String(50), nullable=False)
    KYC_DOCUMENT_EXTENSION_ID = Column(String(50))
    DOCUMENT_LINK_ID = Column(String(50), nullable=False)
    DOCUMENT_TYPE = Column(String(50), nullable=False)
    DOCUMENT_SUB_TYPE = Column(String(50))
    DOCUMENT_NAME = Column(String(255), nullable=False)
    DOCUMENT_S3_LOCATION = Column(String(255))
    INNER_DOCUMENT_ID = Column(String(50))
    INNER_DOCUMENT = Column(String(255))
    BATCH_ID = Column(String(50), nullable=False)
    BATCH_DT = Column(Date, nullable=False)
    CREATE_ID = Column(String(50))
    CREATE_DT = Column(Date, nullable=False)

# Create all tables in the database
Base.metadata.create_all(bind=engine)
