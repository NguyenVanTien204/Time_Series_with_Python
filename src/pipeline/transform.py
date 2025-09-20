import pandas as pd

from src.pipeline.ingest import DataIngestor
from src.pipeline.load import Loader

class Transformation_Engine:
    """
    A class to handle data transformation tasks.
    """

    @staticmethod
    def transform_csv_to_db(file_path: str, table_name: str) -> pd.DataFrame:

        # Ingest data from CSV
        df = DataIngestor.ingest_data(file_path)

        # Load data to database
        Loader.load_result(df, table_name)

        return df
