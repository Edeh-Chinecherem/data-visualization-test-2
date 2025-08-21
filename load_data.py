import pandas as pd

def load_clean_data(file_path):
    """
    Load and clean the e-commerce transaction data from Excel file
    """
    # Read the Excel file with the specific sheet name
    df = pd.read_excel(file_path, sheet_name='Dummy_E-commerce_Transactions.c')
    
    # Clean column names (remove any extra spaces)
    df.columns = df.columns.str.strip()
    
    # Convert Transaction Date to datetime
    df['Transaction Date'] = pd.to_datetime(df['Transaction Date'])
    
    print(f"Data loaded successfully! Shape: {df.shape}")
    return df