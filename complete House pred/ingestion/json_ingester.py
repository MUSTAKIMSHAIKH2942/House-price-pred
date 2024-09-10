# import pandas as pd
# from ingest.base import BaseIngester

# class JSONDataIngester(BaseIngester):
#     def ingest(self, file_path: str) -> pd.DataFrame:
#         try:
#             df = pd.read_json(file_path)
#             return df
#         except Exception as e:
#             raise ValueError(f"Error reading JSON file: {e}")
