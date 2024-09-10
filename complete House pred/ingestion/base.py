# # ingest/base.py
# from abc import ABC, abstractmethod
# import pandas as pd

# class BaseIngester(ABC):
#     @abstractmethod
#     def ingest(self, file_path: str) -> pd.DataFrame:
#         """Abstract method for ingesting data into a DataFrame"""
#         pass

# # class CSVDataIngester(BaseIngester):
# #     def ingest(self, file_path: str) -> pd.DataFrame:
# #         try:
# #             df = pd.read_csv(file_path)
# #             return df
# #         except Exception as e:
# #             raise ValueError(f"Error reading CSV file: {e}")

# # class JSONDataIngester(BaseIngester):
# #     def ingest(self, file_path: str) -> pd.DataFrame:
# #         try:
# #             df = pd.read_json(file_path)
# #             return df
# #         except Exception as e:
# #             raise ValueError(f"Error reading JSON file: {e}")

