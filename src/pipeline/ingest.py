import pandas as pd
import numpy as np

class DataIngestor:
    """
    A class to handle data ingestion from various sources.
    """

    @staticmethod
    def ingest_data(file_path: str) -> pd.DataFrame:
        """
        Ingest data from a CSV file.

        Parameters:
        file_path (str): The path to the CSV file.

        Returns:
        pd.DataFrame: The ingested data as a pandas DataFrame.
        """
        try:
            data = pd.read_csv(file_path)
            return data
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
            return pd.DataFrame()
