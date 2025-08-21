import pandas as pd

def assign_engagement_tiers(df):
    """
    Calculate previous purchases and assign engagement tiers
    """
    # Sort by customer and date to ensure chronological order
    df = df.sort_values(['Customer ID', 'Transaction Date']).copy()
    
    # Calculate previous purchases for each customer
    df['Previous Purchases'] = df.groupby('Customer ID').cumcount()
    
    # Assign engagement tiers based on previous purchases
    df['Engagement Tier'] = pd.cut(df['Previous Purchases'], 
                                   bins=[-1, 0, 4, float('inf')], 
                                   labels=['New', 'Active', 'Power User'])
    
    return df

def calculate_revenue_by_tier(df):
    """
    Calculate total revenue by engagement tier
    """
    revenue_by_tier = df.groupby('Engagement Tier')['Transaction Amount'].sum().round(2)
    return revenue_by_tier