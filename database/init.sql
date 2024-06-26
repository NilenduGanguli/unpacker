
CREATE TABLE IF NOT EXISTS users (
    SOEID VARCHAR(7) PRIMARY KEY,
    ENTITLEMENT_CATEGORY VARCHAR(50) NOT NULL ,
    ENTITLEMENT_LEVEL VARCHAR(50) NOT NULL 
);

CREATE TABLE IF NOT EXISTS KYC_DOCUMENT (
    KYC_DOCUMENT_ID VARCHAR(50) PRIMARY KEY,
    DOCUMENT_COMPONENT_STATE VARCHAR(50) NOT NULL,
    DOCUMENT_LINK_ID VARCHAR(50) NOT NULL,
    DOCUMENT_TYPE VARCHAR(50) NOT NULL,
    DOCUMENT_SUB_TYPE VARCHAR(50) ,
    DOCUMENT_NAME VARCHAR(255) NOT NULL,
    DOCUMENT_LOCATION VARCHAR(255) ,
    CREATE_ID VARCHAR(50) ,
    CREATE_DT DATE NOT NULL
);

CREATE TABLE IF NOT EXISTS KYC_DOCUMENT_TRANSFER (
    KYC_DOCUMENT_ID VARCHAR(50) PRIMARY KEY,
    DOCUMENT_COMPONENT_STATE VARCHAR(50) NOT NULL,
    DOCUMENT_LINK_ID VARCHAR(50) NOT NULL,
    DOCUMENT_NAME VARCHAR(255) NOT NULL,
    DOCUMENT_S3_LOCATION VARCHAR(255) ,
    BATCH_ID VARCHAR(50) NOT NULL,
    BATCH_DT DATE NOT NULL ,
    CREATE_ID VARCHAR(50) ,
    CREATE_DT DATE NOT NULL
);

CREATE TABLE IF NOT EXISTS KYC_DOCUMENT_EXTENSION (
    KYC_DOCUMENT_ID VARCHAR(50) PRIMARY KEY,
    DOCUMENT_COMPONENT_STATE VARCHAR(50) NOT NULL,
    KYC_DOCUMENT_EXTENSION_ID VARCHAR(50) ,
    DOCUMENT_LINK_ID VARCHAR(50) NOT NULL,
    DOCUMENT_TYPE VARCHAR(50) NOT NULL,
    DOCUMENT_SUB_TYPE VARCHAR(50) ,
    DOCUMENT_NAME VARCHAR(255) NOT NULL,
    DOCUMENT_S3_LOCATION VARCHAR(255) ,
    INNER_DOCUMENT_ID VARCHAR(50) ,
    INNER_DOCUMENT VARCHAR(255) ,
    BATCH_ID VARCHAR(50) NOT NULL,
    BATCH_DT DATE NOT NULL ,
    CREATE_ID VARCHAR(50) ,
    CREATE_DT DATE NOT NULL
);