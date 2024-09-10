# # ingest/factory.py
# from ingest.csv_ingester import CSVIngester
# from ingest.json_ingester import JSONIngester
# from ingest.zip_ingester import ZIPIngester

# class IngestionFactory:
#     @staticmethod
#     def get_ingester(file_path: str):
#         if file_path.endswith('.csv'):
#             return CSVIngester()
#         elif file_path.endswith('.json'):
#             return JSONIngester()
#         elif file_path.endswith('.zip'):
#             return ZIPIngester()
#         else:
#             raise ValueError("Unsupported file format.")
