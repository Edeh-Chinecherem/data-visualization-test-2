import matplotlib.pyplot as plt
import pandas as pd

def create_trend_chart(df):
    """
    Create multi-line chart showing monthly revenue trends by Region
    """
    # Create Month-Year period for grouping
    df['Month-Year'] = df['Transaction Date'].dt.to_period('M')
    
    # Calculate monthly revenue by region
    monthly_revenue = df.groupby(['Month-Year', 'Region'])['Transaction Amount'].sum().unstack()
    
    # Create the plot
    plt.figure(figsize=(15, 8))
    for region in monthly_revenue.columns:
        plt.plot(monthly_revenue.index.astype(str), monthly_revenue[region], 
                 marker='o', label=region, linewidth=2, markersize=4)

    plt.title('Monthly Revenue Trends by Region (Jan 2022 - Dec 2024)', fontsize=14, fontweight='bold')
    plt.xlabel('Month-Year', fontsize=12)
    plt.ylabel('Revenue ($)', fontsize=12)
    plt.legend(title='Region', title_fontsize=12, fontsize=10)
    plt.xticks(rotation=45, ha='right')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

def create_category_chart(df):
    """
    Create bar chart comparing revenue  by Category for 2024
    """
    # Filter for 2024 data only
    df_2024 = df[df['Transaction Date'].dt.year == 2024].copy()
    
    # Calculate revenue by category
    category_revenue_2024 = df_2024.groupby('Category')['Transaction Amount'].sum().sort_values(ascending=False)
    
    # Create the plot
    plt.figure(figsize=(12, 6))
    bars = plt.bar(category_revenue_2024.index, category_revenue_2024.values, color='skyblue')
    
    # Add value labels on bars
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height + 100,
                f'${height:,.0f}', ha='center', va='bottom', fontsize=10)

    plt.title('Revenue by Category (2024)', fontsize=14, fontweight='bold')
    plt.xlabel('Category', fontsize=12)
    plt.ylabel('Revenue ($)', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.show()