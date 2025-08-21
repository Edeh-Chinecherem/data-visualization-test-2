from load_data import load_clean_data
from calculate_engagement import assign_engagement_tiers, calculate_revenue_by_tier
from create_visualizations import create_trend_chart, create_category_chart

def main():
    # Load the data
    file_path = "Ecom Q4 Dataset - Public.xlsx"
    df = load_clean_data(file_path)
    
    # Calculate engagement tiers
    df_with_tiers = assign_engagement_tiers(df)
    
    # Calculate and display revenue by tier
    revenue_by_tier = calculate_revenue_by_tier(df_with_tiers)
    
    print("=" * 50)
    print("TOTAL REVENUE BY ENGAGEMENT TIER")
    print("=" * 50)
    for tier, revenue in revenue_by_tier.items():
        print(f"{tier:12}: ${revenue:,.2f}")
    
    total_revenue = revenue_by_tier.sum()
    print("-" * 50)
    print(f"{'Grand Total':12}: ${total_revenue:,.2f}")
    print("=" * 50)
    
    # Create visualizations
    print("\nGenerating visualizations...")
    create_trend_chart(df_with_tiers)
    create_category_chart(df_with_tiers)
    
    # Optional: Save the enriched data to a new Excel file
    df_with_tiers.to_excel('ecommerce_data_with_tiers.xlsx', index=False)
    print("Enriched data saved to 'ecommerce_data_with_tiers.xlsx'")

if __name__ == "__main__":
    main()