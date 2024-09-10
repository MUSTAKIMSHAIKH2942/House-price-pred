# import zipfile
# import os
# import pandas as pd
# from ingest.base import BaseIngester

# class ZipFileDataIngester(BaseIngester):
#     def ingest(self, file_path: str) -> pd.DataFrame:
#         if not zipfile.is_zipfile(file_path):
#             raise ValueError("The provided file is not a zip file.")
        
#         with zipfile.ZipFile(file_path, 'r') as zip_ref:
#             zip_ref.extractall('extracted_data')
#             csv_files = [f for f in os.listdir('extracted_data') if f.endswith('.csv')]
            
#             if len(csv_files) == 0:
#                 raise FileNotFoundError("No CSV files found in the zip archive.")
#             elif len(csv_files) > 1:
#                 raise ValueError("Multiple CSV files found in the zip archive. Specify which one to use.")
            
#             csv_path = os.path.join('extracted_data', csv_files[0])
#             return pd.read_csv(csv_path)
