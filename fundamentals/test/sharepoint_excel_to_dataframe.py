import pandas as pd
import requests
import os
import re
from urllib.parse import urlparse, unquote
from docx import Document
from io import BytesIO
import tempfile
from test_markdown_to_pandas_df import SharePointClient


class SharePointExcelProcessor:
    def __init__(self, tenant_id, client_id, client_secret, resource_url):
        """
        Initialize the SharePoint Excel processor with SharePoint client.
        
        Args:
            tenant_id: Azure AD tenant ID
            client_id: Azure AD application client ID
            client_secret: Azure AD application client secret
            resource_url: SharePoint resource URL (e.g., 'https://yourtenant.sharepoint.com')
        """
        self.sharepoint_client = SharePointClient(tenant_id, client_id, client_secret, resource_url)
        self.resource_url = resource_url
        
    def get_site_and_drive_info(self, site_name):
        """
        Get site ID and drive ID for the specified SharePoint site.
        
        Args:
            site_name: Name of the SharePoint site (e.g., 'onBehalf')
            
        Returns:
            tuple: (site_id, drive_id) or (None, None) if not found
        """
        # Construct the site URL - you may need to adjust this based on your SharePoint structure
        site_url = f"{self.resource_url.replace('https://', '')}/sites/{site_name}"
        
        try:
            site_id = self.sharepoint_client.get_site_id(site_url)
            if not site_id:
                print(f"Could not find site ID for {site_name}")
                return None, None
                
            drives = self.sharepoint_client.get_drive_id(site_id)
            # Look for the Documents drive
            drive_id = None
            for drive_id_temp, drive_name in drives:
                if 'Documents' in drive_name or 'Shared Documents' in drive_name:
                    drive_id = drive_id_temp
                    break
            
            if not drive_id and drives:
                # Use the first drive if no Documents drive found
                drive_id = drives[0][0]
                
            return site_id, drive_id
            
        except Exception as e:
            print(f"Error getting site and drive info: {e}")
            return None, None
    
    def download_excel_file(self, site_id, drive_id, excel_filename="summarization_feedback.xlsx"):
        """
        Download the Excel file from SharePoint Documents folder.
        
        Args:
            site_id: SharePoint site ID
            drive_id: SharePoint drive ID
            excel_filename: Name of the Excel file
            
        Returns:
            str: Path to the downloaded Excel file, or None if failed
        """
        try:
            # Get root folder contents
            folder_contents = self.sharepoint_client.get_folder_content(site_id, drive_id)
            
            # Find the Excel file
            file_id = None
            for item_id, item_name in folder_contents:
                if item_name == excel_filename:
                    file_id = item_id
                    break
            
            if not file_id:
                print(f"Excel file {excel_filename} not found in Documents")
                return None
            
            # Download the file
            temp_dir = tempfile.mkdtemp()
            file_path = os.path.join(temp_dir, excel_filename)
            
            download_url = f"https://graph.microsoft.com/v1.0/sites/{site_id}/drives/{drive_id}/items/{file_id}/content"
            self.sharepoint_client.download_file(download_url, temp_dir, excel_filename)
            
            return file_path
            
        except Exception as e:
            print(f"Error downloading Excel file: {e}")
            return None
    
    def parse_sharepoint_url(self, url):
        """
        Parse SharePoint URL to extract site, drive, and file path information.
        
        Args:
            url: SharePoint URL pointing to a Word document
            
        Returns:
            dict: Parsed URL components or None if parsing fails
        """
        try:
            # SharePoint URLs typically look like:
            # https://tenant.sharepoint.com/sites/sitename/_layouts/15/Doc.aspx?sourcedoc={guid}&file=filename.docx
            # or
            # https://tenant.sharepoint.com/sites/sitename/Shared%20Documents/path/filename.docx
            
            parsed_url = urlparse(url)
            
            # Extract site name from path
            path_parts = parsed_url.path.split('/')
            if 'sites' in path_parts:
                site_index = path_parts.index('sites')
                if site_index + 1 < len(path_parts):
                    site_name = path_parts[site_index + 1]
                else:
                    return None
            else:
                return None
            
            # Handle different URL formats
            if 'sourcedoc' in parsed_url.query:
                # Format: Doc.aspx?sourcedoc={guid}&file=filename.docx
                import urllib.parse
                query_params = urllib.parse.parse_qs(parsed_url.query)
                if 'file' in query_params:
                    filename = query_params['file'][0]
                    return {
                        'site_name': site_name,
                        'filename': filename,
                        'file_path': f"Documents/Apps/Microsoft Forms/onBehalf Summary/Long summary/{filename}"
                    }
            else:
                # Direct file path format
                # Decode URL-encoded path
                decoded_path = unquote(parsed_url.path)
                path_parts = decoded_path.split('/')
                
                # Find the filename (last part)
                filename = path_parts[-1] if path_parts else None
                
                return {
                    'site_name': site_name,
                    'filename': filename,
                    'file_path': decoded_path
                }
            
            return None
            
        except Exception as e:
            print(f"Error parsing URL {url}: {e}")
            return None
    
    def find_file_in_sharepoint(self, site_id, drive_id, target_filename):
        """
        Recursively search for a file in SharePoint.
        
        Args:
            site_id: SharePoint site ID
            drive_id: SharePoint drive ID
            target_filename: Name of the file to find
            
        Returns:
            str: File ID if found, None otherwise
        """
        try:
            # Start from root and search recursively
            return self._search_folder_for_file(site_id, drive_id, "root", target_filename)
        except Exception as e:
            print(f"Error searching for file {target_filename}: {e}")
            return None
    
    def _search_folder_for_file(self, site_id, drive_id, folder_id, target_filename):
        """
        Recursively search for a file in a specific folder.
        
        Args:
            site_id: SharePoint site ID
            drive_id: SharePoint drive ID
            folder_id: Folder ID to search in
            target_filename: Name of the file to find
            
        Returns:
            str: File ID if found, None otherwise
        """
        try:
            folder_contents_url = f'https://graph.microsoft.com/v1.0/sites/{site_id}/drives/{drive_id}/items/{folder_id}/children'
            headers = {'Authorization': f'Bearer {self.sharepoint_client.access_token}'}
            response = requests.get(folder_contents_url, headers=headers)
            
            if response.status_code != 200:
                return None
                
            folder_contents = response.json()
            
            if 'value' in folder_contents:
                for item in folder_contents['value']:
                    if 'file' in item and item['name'] == target_filename:
                        return item['id']
                    elif 'folder' in item:
                        # Recursively search subfolders
                        result = self._search_folder_for_file(site_id, drive_id, item['id'], target_filename)
                        if result:
                            return result
            
            return None
            
        except Exception as e:
            print(f"Error searching folder for file: {e}")
            return None
    
    def download_and_extract_word_content(self, site_id, drive_id, file_id):
        """
        Download a Word document and extract its text content.
        
        Args:
            site_id: SharePoint site ID
            drive_id: SharePoint drive ID
            file_id: Word document file ID
            
        Returns:
            str: Extracted text content or None if failed
        """
        try:
            # Download the Word document
            download_url = f"https://graph.microsoft.com/v1.0/sites/{site_id}/drives/{drive_id}/items/{file_id}/content"
            headers = {'Authorization': f'Bearer {self.sharepoint_client.access_token}'}
            response = requests.get(download_url, headers=headers)
            
            if response.status_code != 200:
                print(f"Failed to download Word document: {response.status_code}")
                return None
            
            # Extract text from Word document
            doc = Document(BytesIO(response.content))
            text_content = []
            
            for paragraph in doc.paragraphs:
                text_content.append(paragraph.text)
            
            return '\n'.join(text_content)
            
        except Exception as e:
            print(f"Error extracting Word content: {e}")
            return None
    
    def process_excel_to_dataframe(self, site_name="onBehalf", excel_filename="summarization_feedback.xlsx"):
        """
        Main method to process Excel file and add Word document content.
        
        Args:
            site_name: Name of the SharePoint site
            excel_filename: Name of the Excel file
            
        Returns:
            pd.DataFrame: DataFrame with original data plus Word document content
        """
        try:
            # Get site and drive information
            site_id, drive_id = self.get_site_and_drive_info(site_name)
            if not site_id or not drive_id:
                print("Could not get site and drive information")
                return None
            
            # Download the Excel file
            excel_path = self.download_excel_file(site_id, drive_id, excel_filename)
            if not excel_path:
                print("Could not download Excel file")
                return None
            
            # Read Excel file into DataFrame
            df = pd.read_excel(excel_path)
            
            # Add a new column for Word document content
            df['word_content'] = ""
            
            # Process each URL in column A
            for index, row in df.iterrows():
                url = row.iloc[0]  # Column A is the first column
                
                if pd.isna(url) or not url:
                    continue
                
                print(f"Processing URL {index + 1}: {url}")
                
                # Parse the SharePoint URL
                parsed_info = self.parse_sharepoint_url(url)
                if not parsed_info:
                    print(f"Could not parse URL: {url}")
                    continue
                
                # Find the Word document in SharePoint
                filename = parsed_info['filename']
                file_id = self.find_file_in_sharepoint(site_id, drive_id, filename)
                
                if not file_id:
                    print(f"Could not find file: {filename}")
                    continue
                
                # Download and extract Word content
                content = self.download_and_extract_word_content(site_id, drive_id, file_id)
                if content:
                    df.at[index, 'word_content'] = content
                    print(f"Successfully extracted content for: {filename}")
                else:
                    print(f"Could not extract content for: {filename}")
            
            # Clean up temporary files
            if os.path.exists(excel_path):
                os.remove(excel_path)
            
            return df
            
        except Exception as e:
            print(f"Error processing Excel to DataFrame: {e}")
            return None


def main():
    """
    Example usage of the SharePointExcelProcessor.
    """
    # Replace with your actual credentials
    tenant_id = "your-tenant-id"
    client_id = "your-client-id"
    client_secret = "your-client-secret"
    resource_url = "https://yourtenant.sharepoint.com"
    
    # Initialize the processor
    processor = SharePointExcelProcessor(tenant_id, client_id, client_secret, resource_url)
    
    # Process the Excel file
    df = processor.process_excel_to_dataframe(site_name="onBehalf", excel_filename="summarization_feedback.xlsx")
    
    if df is not None:
        print("Successfully processed Excel file!")
        print(f"DataFrame shape: {df.shape}")
        print("\nColumn names:")
        print(df.columns.tolist())
        
        # Display first few rows
        print("\nFirst 3 rows:")
        print(df.head(3))
        
        # Save to CSV for further analysis
        df.to_csv("processed_summarization_feedback.csv", index=False)
        print("\nDataFrame saved to processed_summarization_feedback.csv")
    else:
        print("Failed to process Excel file")


if __name__ == "__main__":
    main() 