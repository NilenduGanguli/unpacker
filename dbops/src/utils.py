import httpx
from datetime import date

BASE_URL = "http://localhost:8000"  # Replace with your FastAPI server URL

# Function to add a row to the 'users' table
def add_user(soeid, entitlement_category, entitlement_level):
    url = f"{BASE_URL}/users/"
    data = {
        "SOEID": soeid,
        "ENTITLEMENT_CATEGORY": entitlement_category,
        "ENTITLEMENT_LEVEL": entitlement_level
    }
    response = httpx.post(url, json=data)
    return response.json()

# Function to update a row in the 'users' table
def update_user(soeid, entitlement_category, entitlement_level):
    url = f"{BASE_URL}/users/{soeid}"
    data = {
        "ENTITLEMENT_CATEGORY": entitlement_category,
        "ENTITLEMENT_LEVEL": entitlement_level
    }
    response = httpx.put(url, json=data)
    return response.json()

# Function to add a row to the 'KYC_DOCUMENT' table
def add_kyc_document(kyc_document_id, document_component_state, document_link_id, document_type, document_sub_type, document_name, document_location, create_id, create_dt):
    url = f"{BASE_URL}/kyc_document/"
    data = {
        "KYC_DOCUMENT_ID": kyc_document_id,
        "DOCUMENT_COMPONENT_STATE": document_component_state,
        "DOCUMENT_LINK_ID": document_link_id,
        "DOCUMENT_TYPE": document_type,
        "DOCUMENT_SUB_TYPE": document_sub_type,
        "DOCUMENT_NAME": document_name,
        "DOCUMENT_LOCATION": document_location,
        "CREATE_ID": create_id,
        "CREATE_DT": create_dt.isoformat()
    }
    response = httpx.post(url, json=data)
    return response.json()

# Function to update a row in the 'KYC_DOCUMENT' table
def update_kyc_document(kyc_document_id, document_component_state, document_link_id, document_type, document_sub_type, document_name, document_location, create_id, create_dt):
    url = f"{BASE_URL}/kyc_document/{kyc_document_id}"
    data = {
        "DOCUMENT_COMPONENT_STATE": document_component_state,
        "DOCUMENT_LINK_ID": document_link_id,
        "DOCUMENT_TYPE": document_type,
        "DOCUMENT_SUB_TYPE": document_sub_type,
        "DOCUMENT_NAME": document_name,
        "DOCUMENT_LOCATION": document_location,
        "CREATE_ID": create_id,
        "CREATE_DT": create_dt.isoformat()
    }
    response = httpx.put(url, json=data)
    return response.json()

# Function to add a row to the 'KYC_DOCUMENT_TRANSFER' table
def add_kyc_document_transfer(kyc_document_id, document_component_state, document_link_id, document_name, document_s3_location, batch_id, batch_dt, create_id, create_dt):
    url = f"{BASE_URL}/kyc_document_transfer/"
    data = {
        "KYC_DOCUMENT_ID": kyc_document_id,
        "DOCUMENT_COMPONENT_STATE": document_component_state,
        "DOCUMENT_LINK_ID": document_link_id,
        "DOCUMENT_NAME": document_name,
        "DOCUMENT_S3_LOCATION": document_s3_location,
        "BATCH_ID": batch_id,
        "BATCH_DT": batch_dt.isoformat(),
        "CREATE_ID": create_id,
        "CREATE_DT": create_dt.isoformat()
    }
    response = httpx.post(url, json=data)
    return response.json()

# Function to update a row in the 'KYC_DOCUMENT_TRANSFER' table
def update_kyc_document_transfer(kyc_document_id, document_component_state, document_link_id, document_name, document_s3_location, batch_id, batch_dt, create_id, create_dt):
    url = f"{BASE_URL}/kyc_document_transfer/{kyc_document_id}"
    data = {
        "DOCUMENT_COMPONENT_STATE": document_component_state,
        "DOCUMENT_LINK_ID": document_link_id,
        "DOCUMENT_NAME": document_name,
        "DOCUMENT_S3_LOCATION": document_s3_location,
        "BATCH_ID": batch_id,
        "BATCH_DT": batch_dt.isoformat(),
        "CREATE_ID": create_id,
        "CREATE_DT": create_dt.isoformat()
    }
    response = httpx.put(url, json=data)
    return response.json()

# Function to add a row to the 'KYC_DOCUMENT_EXTENSION' table
def add_kyc_document_extension(kyc_document_id, document_component_state, kyc_document_extension_id, document_link_id, document_type, document_sub_type, document_name, document_s3_location, inner_document_id, inner_document, batch_id, batch_dt, create_id, create_dt):
    url = f"{BASE_URL}/kyc_document_extension/"
    data = {
        "KYC_DOCUMENT_ID": kyc_document_id,
        "DOCUMENT_COMPONENT_STATE": document_component_state,
        "KYC_DOCUMENT_EXTENSION_ID": kyc_document_extension_id,
        "DOCUMENT_LINK_ID": document_link_id,
        "DOCUMENT_TYPE": document_type,
        "DOCUMENT_SUB_TYPE": document_sub_type,
        "DOCUMENT_NAME": document_name,
        "DOCUMENT_S3_LOCATION": document_s3_location,
        "INNER_DOCUMENT_ID": inner_document_id,
        "INNER_DOCUMENT": inner_document,
        "BATCH_ID": batch_id,
        "BATCH_DT": batch_dt.isoformat(),
        "CREATE_ID": create_id,
        "CREATE_DT": create_dt.isoformat()
    }
    response = httpx.post(url, json=data)
    return response.json()

# Function to update a row in the 'KYC_DOCUMENT_EXTENSION' table
def update_kyc_document_extension(kyc_document_id, document_component_state, kyc_document_extension_id, document_link_id, document_type, document_sub_type, document_name, document_s3_location, inner_document_id, inner_document, batch_id, batch_dt, create_id, create_dt):
    url = f"{BASE_URL}/kyc_document_extension/{kyc_document_id}"
    data = {
        "DOCUMENT_COMPONENT_STATE": document_component_state,
        "KYC_DOCUMENT_EXTENSION_ID": kyc_document_extension_id,
        "DOCUMENT_LINK_ID": document_link_id,
        "DOCUMENT_TYPE": document_type,
        "DOCUMENT_SUB_TYPE": document_sub_type,
        "DOCUMENT_NAME": document_name,
        "DOCUMENT_S3_LOCATION": document_s3_location,
        "INNER_DOCUMENT_ID": inner_document_id,
        "INNER_DOCUMENT": inner_document,
        "BATCH_ID": batch_id,
        "BATCH_DT": batch_dt.isoformat(),
        "CREATE_ID": create_id,
        "CREATE_DT": create_dt.isoformat()
    }
    response = httpx.put(url, json=data)
    return response.json()

# Example usage
if __name__ == "__main__":
    # Add a new user
    print(add_user("U123456", "Category1", "Level1"))
    
    # Update an existing user
    print(update_user("U123456", "Category2", "Level2"))
    
    # Add a new KYC document
    print(add_kyc_document("D123", "State1", "Link1", "Type1", "SubType1", "Name1", "Location1", "Creator1", date.today()))
    
    # Update an existing KYC document
    print(update_kyc_document("D123", "State2", "Link2", "Type2", "SubType2", "Name2", "Location2", "Creator2", date.today()))
    
    # Add a new KYC document transfer
    print(add_kyc_document_transfer("D124", "State1", "Link1", "Name1", "S3Location1", "Batch1", date.today(), "Creator1", date.today()))
    
    # Update an existing KYC document transfer
    print(update_kyc_document_transfer("D124", "State2", "Link2", "Name2", "S3Location2", "Batch2", date.today(), "Creator2", date.today()))
    
    # Add a new KYC document extension
    print(add_kyc_document_extension("D125", "State1", "Ext1", "Link1", "Type1", "SubType1", "Name1", "S3Location1", "InnerID1", "InnerDoc1", "Batch1", date.today(), "Creator1", date.today()))
    
    # Update an existing KYC document extension
    print(update_kyc_document_extension("D125", "State2", "Ext2", "Link2", "Type2", "SubType2", "Name2", "S3Location2", "InnerID2", "InnerDoc2", "Batch2", date.today(), "Creator2", date.today()))
