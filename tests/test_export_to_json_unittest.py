
# Generated by CodiumAI

# Dependencies:
# pip install pytest-mock
import unittest

class TestExportToJson(unittest.TestCase):

    #  The function successfully connects to the specified database and retrieves data from the specified table.
    def test_connects_to_database_and_retrieves_data(self, mocker):
        # Arrange
        db_name = "test.db"
        table_name = "test_table"
        output_filename = "output.json"
        selected_columns = ["column1", "column2"]
    
        conn_mock = mocker.Mock()
        mocker.patch("sqlite3.connect", return_value=conn_mock)
    
        query = f"SELECT {', '.join(selected_columns)} FROM {table_name}"
        df_mock = mocker.Mock()
        mocker.patch("pandas.read_sql_query", return_value=df_mock)
    
        json_data_mock = mocker.Mock()
        df_mock.to_json.return_value = json_data_mock
    
        # Act
        export_to_json(db_name, table_name, output_filename, selected_columns)
    
        # Assert
        sqlite3.connect.assert_called_once_with(db_name)
        pandas.read_sql_query.assert_called_once_with(query, conn_mock)
        df_mock.to_json.assert_called_once_with(orient="records", indent=4)
        with open(json_filename, 'w') as json_file:
            json_file.write.assert_called_once_with(output_filename)
        conn_mock.close.assert_called_once()

    #  The function successfully exports the retrieved data to a JSON file with the specified output filename.
    def test_exports_data_to_json_file(self, mocker):
        # Arrange
        db_name = "test.db"
        table_name = "test_table"
        output_filename = "output.json"
    
        conn_mock = mocker.Mock()
        mocker.patch("sqlite3.connect", return_value=conn_mock)
    
        query = f"SELECT * FROM {table_name}"
        df_mock = mocker.Mock()
        mocker.patch("pandas.read_sql_query", return_value=df_mock)
    
        json_data_mock = mocker.Mock()
        df_mock.to_json.return_value = json_data_mock
    
        # Act
        export_to_json(db_name, table_name, output_filename)
    
        # Assert
        sqlite3.connect.assert_called_once_with(db_name)
        pandas.read_sql_query.assert_called_once_with(query, conn_mock)
        df_mock.to_json.assert_called_once_with(orient="records", indent=4)
        with open(json_filename, 'w') as json_file:
            json_file.write.assert_called_once_with(output_filename)
        conn_mock.close.assert_called_once()

    #  The function successfully exports all columns of the specified table when no selected columns are specified.
    def test_exports_all_columns_when_no_selected_columns(self, mocker):
        # Arrange
        db_name = "test.db"
        table_name = "test_table"
        output_filename = "output.json"
    
        conn_mock = mocker.Mock()
        mocker.patch("sqlite3.connect", return_value=conn_mock)
    
        query = f"SELECT * FROM {table_name}"
        df_mock = mocker.Mock()
        mocker.patch("pandas.read_sql_query", return_value=df_mock)
    
        json_data_mock = mocker.Mock()
        df_mock.to_json.return_value = json_data_mock
    
        # Act
        export_to_json(db_name, table_name, output_filename)
    
        # Assert
        sqlite3.connect.assert_called_once_with(db_name)
        pandas.read_sql_query.assert_called_once_with(query, conn_mock)
        df_mock.to_json.assert_called_once_with(orient="records", indent=4)
        with open(json_filename, 'w') as json_file:
            json_file.write.assert_called_once_with(output_filename)
        conn_mock.close.assert_called_once()

    #  The specified database does not exist.
    def test_database_does_not_exist(self, mocker):
        # Arrange
        db_name = "nonexistent.db"
        table_name = "test_table"
        output_filename = "output.json"
    
        mocker.patch("sqlite3.connect", side_effect=sqlite3.OperationalError)
    
        # Act & Assert
        with self.assertRaises(sqlite3.OperationalError):
            export_to_json(db_name, table_name, output_filename)

    #  The specified table does not exist in the specified database.
    def test_table_does_not_exist(self, mocker):
        # Arrange
        db_name = "test.db"
        table_name = "nonexistent_table"
        output_filename = "output.json"
    
        conn_mock = mocker.Mock()
        mocker.patch("sqlite3.connect", return_value=conn_mock)
    
        mocker.patch("pandas.read_sql_query", side_effect=pd.io.sql.DatabaseError)
    
        # Act & Assert
        with self.assertRaises(pd.io.sql.DatabaseError):
            export_to_json(db_name, table_name, output_filename)

    #  The specified selected columns do not exist in the specified table.
    def test_selected_columns_do_not_exist(self, mocker):
        # Arrange
        db_name = "test.db"
        table_name = "test_table"
        output_filename = "output.json"
        selected_columns = ["nonexistent_column"]
    
        conn_mock = mocker.Mock()
        mocker.patch("sqlite3.connect", return_value=conn_mock)
    
        query = f"SELECT {', '.join(selected_columns)} FROM {table_name}"
        mocker.patch("pandas.read_sql_query", side_effect=pd.io.sql.DatabaseError)
    
        # Act & Assert
        with self.assertRaises(pd.io.sql.DatabaseError):
            export_to_json(db_name, table_name, output_filename, selected_columns)