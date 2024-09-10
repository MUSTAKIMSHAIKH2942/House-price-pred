# import pandas as pd
# from ingest.base import BaseIngester

# class CSVDataIngester(BaseIngester):
#     def ingest(self, file_path: str) -> pd.DataFrame:
#         try:
#             df = pd.read_csv(file_path)
#             return df
#         except Exception as e:
#             raise ValueError(f"Error reading CSV file: {e}")



# # ingest/csv_ingester.py
# # import pandas as pd
# # from ingest.base import BaseIngester

# # class CSVIngester(BaseIngester):
# #     def ingest(self, file_path: str) -> pd.DataFrame:
# #         return pd.read_csv(file_path)
