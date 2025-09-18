import pandas as pd
import os
from sqlalchemy import create_engine
from src.utils.conection import postgres_connection

class Loader:
    """
    A class to load data from various file formats.
    """

    @staticmethod


    def load_csv_to_postgres(file_path: str, table_name: str = None, if_exists: str = "replace"):
        """
        Load data from a CSV file and create a PostgreSQL table with inferred columns.

        Parameters:
        file_path (str): Path to the CSV file.
        engine_url (str): SQLAlchemy engine URL for PostgreSQL (e.g., 'postgresql+psycopg2://user:pass@localhost:5432/dbname')
        table_name (str): Optional, name of the table in Postgres. Defaults to CSV file name.
        if_exists (str): Behavior if the table already exists. Options: 'fail', 'replace', 'append'. Default: 'replace'.

        Returns:
        int: Number of rows inserted.
        """
        try:
            # 1. Đọc CSV
            df = pd.read_csv(file_path)

            if df.empty:
                print("CSV is empty. No table created.")
                return 0

            # 2. Lấy tên bảng mặc định từ tên file
            if table_name is None:
                table_name = os.path.splitext(os.path.basename(file_path))[0]

            # 3. Tạo engine kết nối Postgres
            engine = postgres_connection()

            # 4. Đẩy dữ liệu vào Postgres, pandas sẽ tự tạo schema dựa vào dtype
            df.to_sql(table_name, engine, index=False, if_exists=if_exists)

            print(f"Successfully loaded {len(df)} rows into table '{table_name}'.")
            return len(df)

        except Exception as e:
            print(f"Error processing {file_path}: {e}")
            return 0


    @staticmethod
    def load_result(dataframe: pd.DataFrame, tablename: str) -> None:
        """ Load data to a database table."""
        try:
            # Get database connection
            engine = postgres_connection()
            if engine is not None:
                # Load DataFrame to SQL table
                dataframe.to_sql(tablename, con=engine, if_exists='replace', index=False)
                print(f"Data loaded to {tablename} successfully.")
            else:
                print("Failed to establish database connection.")
        except Exception as e:
            print(f"Error loading data to {tablename}: {e}")
