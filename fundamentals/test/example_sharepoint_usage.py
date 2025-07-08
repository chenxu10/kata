#!/usr/bin/env python3
"""
Example usage of SharePointExcelProcessor to process Excel files with Word document links.

This script demonstrates how to:
1. Connect to SharePoint using Microsoft Graph API
2. Download an Excel file from SharePoint
3. Parse SharePoint URLs to Word documents
4. Extract content from Word documents
5. Create a pandas DataFrame with the extracted content

Before running this script, make sure to:
1. Install required dependencies: pip install -r requirements_sharepoint.txt
2. Set up your Azure AD application with appropriate permissions
3. Update the credentials and site information below
"""

from sharepoint_excel_to_dataframe import SharePointExcelProcessor
import pandas as pd
import os

def main():
    # Configuration - UPDATE THESE VALUES
    TENANT_ID = "your-tenant-id-here"  # Azure AD tenant ID
    CLIENT_ID = "your-client-id-here"  # Azure AD application client ID
    CLIENT_SECRET = "your-client-secret-here"  # Azure AD application client secret
    RESOURCE_URL = "https://yourtenant.sharepoint.com"  # Your SharePoint tenant URL
    
    # SharePoint site and file information
    SITE_NAME = "onBehalf"  # Name of your SharePoint site
    EXCEL_FILENAME = "summarization_feedback.xlsx"  # Name of the Excel file
    
    print("SharePoint Excel Processor Example")
    print("=" * 40)
    
    # Initialize the processor
    print("1. Initializing SharePoint connection...")
    try:
        processor = SharePointExcelProcessor(
            tenant_id=TENANT_ID,
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            resource_url=RESOURCE_URL
        )
        print("   ✓ Connection initialized successfully")
    except Exception as e:
        print(f"   ✗ Failed to initialize connection: {e}")
        return
    
    # Process the Excel file
    print("\n2. Processing Excel file...")
    try:
        df = processor.process_excel_to_dataframe(
            site_name=SITE_NAME,
            excel_filename=EXCEL_FILENAME
        )
        
        if df is not None:
            print("   ✓ Excel file processed successfully!")
            print(f"   DataFrame shape: {df.shape}")
            print(f"   Columns: {list(df.columns)}")
            
            # Display summary information
            print("\n3. Processing Summary:")
            print(f"   - Total rows: {len(df)}")
            print(f"   - Rows with Word content: {df['word_content'].notna().sum()}")
            print(f"   - Rows without Word content: {df['word_content'].isna().sum()}")
            
            # Show first few rows (without full content to avoid clutter)
            print("\n4. Sample Data (first 3 rows):")
            sample_df = df.head(3).copy()
            if 'word_content' in sample_df.columns:
                # Truncate content for display
                sample_df['word_content'] = sample_df['word_content'].apply(
                    lambda x: str(x)[:100] + "..." if pd.notna(x) and len(str(x)) > 100 else x
                )
            print(sample_df.to_string(index=False))
            
            # Save the results
            output_file = "processed_summarization_feedback.csv"
            df.to_csv(output_file, index=False)
            print(f"\n5. Results saved to: {output_file}")
            
            # Optional: Save as Excel file
            excel_output_file = "processed_summarization_feedback.xlsx"
            df.to_excel(excel_output_file, index=False)
            print(f"   Results also saved to: {excel_output_file}")
            
        else:
            print("   ✗ Failed to process Excel file")
            
    except Exception as e:
        print(f"   ✗ Error processing Excel file: {e}")
        import traceback
        traceback.print_exc()


def test_url_parsing():
    """
    Test the URL parsing functionality with sample URLs.
    """
    print("\nTesting URL parsing...")
    
    # Sample URLs (replace with your actual URL patterns)
    test_urls = [
        "https://yourtenant.sharepoint.com/sites/onBehalf/_layouts/15/Doc.aspx?sourcedoc={12345678-1234-1234-1234-123456789012}&file=sample.docx",
        "https://yourtenant.sharepoint.com/sites/onBehalf/Shared%20Documents/Apps/Microsoft%20Forms/onBehalf%20Summary/Long%20summary/sample.docx"
    ]
    
    processor = SharePointExcelProcessor("test", "test", "test", "https://yourtenant.sharepoint.com")
    
    for url in test_urls:
        result = processor.parse_sharepoint_url(url)
        print(f"URL: {url}")
        print(f"Parsed: {result}")
        print("-" * 50)


if __name__ == "__main__":
    # Run the main processing
    main()
    
    # Uncomment the line below to test URL parsing
    # test_url_parsing() 