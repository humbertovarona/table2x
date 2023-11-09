
import pytest

class TestExportToLibreofficeCalc:

    #  The function should connect to the database and retrieve data successfully.
    def test_connect_to_database_and_retrieve_data_successfully(self):
        # Arrange
        db_name = "test.db"
        table_name = "test_table"
        output_filename = "output.xlsx"
        selected_columns = ["column1", "column2"]
    
        # Act
        export_to_libreoffice_calc(db_name, table_name, output_filename, selected_columns)
    
        # Assert
        # Check if the output file exists and is not empty
        assert os.path.exists(output_filename)
        assert os.path.getsize(output_filename) > 0
        # Check if the data in the output file matches the data in the database
        conn = sqlite3.connect(db_name)
        query = f"SELECT {', '.join(selected_columns)} FROM {table_name}"
        expected_df = pd.read_sql_query(query, conn)
        conn.close()
        actual_df = pd.read_excel(output_filename)
        pd.testing.assert_frame_equal(expected_df, actual_df)

    #  The function should export data to an excel file successfully.
    def test_export_data_to_excel_successfully(self):
        # Arrange
        db_name = "test.db"
        table_name = "test_table"
        output_filename = "output.xlsx"
    
        # Act
        export_to_libreoffice_calc(db_name, table_name, output_filename)
    
        # Assert
        # Check if the output file exists and is not empty
        assert os.path.exists(output_filename)
        assert os.path.getsize(output_filename) > 0
        # Check if the data in the output file matches the data in the database
        conn = sqlite3.connect(db_name)
        query = f"SELECT * FROM {table_name}"
        expected_df = pd.read_sql_query(query, conn)
        conn.close()
        actual_df = pd.read_excel(output_filename)
        pd.testing.assert_frame_equal(expected_df, actual_df)

    #  The function should handle cases where selected_columns is None and export all columns successfully.
    def test_handle_selected_columns_none_successfully(self):
        # Arrange
        db_name = "test.db"
        table_name = "test_table"
        output_filename = "output.xlsx"
    
        # Act
        export_to_libreoffice_calc(db_name, table_name, output_filename, selected_columns=None)
    
        # Assert
        # Check if the output file exists and is not empty
        assert os.path.exists(output_filename)
        assert os.path.getsize(output_filename) > 0
        # Check if the data in the output file matches the data in the database
        conn = sqlite3.connect(db_name)
        query = f"SELECT * FROM {table_name}"
        expected_df = pd.read_sql_query(query, conn)
        conn.close()
        actual_df = pd.read_excel(output_filename)
        pd.testing.assert_frame_equal(expected_df, actual_df)

    #  The function should handle cases where the database name is invalid and raise an appropriate error.
    def test_handle_invalid_database_name(self):
        # Arrange
        db_name = "invalid.db"
        table_name = "test_table"
        output_filename = "output.xlsx"
    
        # Act and Assert
        with pytest.raises(sqlite3.OperationalError):
            export_to_libreoffice_calc(db_name, table_name, output_filename)

    #  The function should handle cases where the table name is invalid and raise an appropriate error.
    def test_handle_invalid_table_name(self):
        # Arrange
        db_name = "test.db"
        table_name = "invalid_table"
        output_filename = "output.xlsx"
    
        # Act and Assert
        with pytest.raises(sqlite3.OperationalError):
            export_to_libreoffice_calc(db_name, table_name, output_filename)

    #  The function should handle cases where the output filename is invalid and raise an appropriate error.
    def test_handle_invalid_output_filename(self):
        # Arrange
        db_name = "test.db"
        table_name = "test_table"
        output_filename = "invalid/output.xlsx"
    
        # Act and Assert
        with pytest.raises(FileNotFoundError):
            export_to_libreoffice_calc(db_name, table_name, output_filename)
