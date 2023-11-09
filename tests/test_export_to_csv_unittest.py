import unittest

class TestExportToCsv(unittest.TestCase):

    #  The function exports data from a given SQLite database table to a CSV file.
    def test_export_all_columns(self):
        # Arrange
        db_name = "test.db"
        table_name = "employees"
        output_filename = "output.csv"
    
        # Act
        export_to_csv(db_name, table_name, output_filename)
    
        # Assert
        # Check if the CSV file is created
        self.assertTrue(os.path.exists(output_filename))
        # Check if the CSV file contains the correct data
        df = pd.read_csv(output_filename)
        self.assertEqual(len(df.columns), 4)
        self.assertEqual(len(df), 3)

    #  The function exports all columns of the table if no specific columns are selected.
    def test_export_all_columns_no_selection(self):
        # Arrange
        db_name = "test.db"
        table_name = "employees"
        output_filename = "output.csv"
    
        # Act
        export_to_csv(db_name, table_name, output_filename)
    
        # Assert
        # Check if the CSV file is created
        self.assertTrue(os.path.exists(output_filename))
        # Check if the CSV file contains the correct data
        df = pd.read_csv(output_filename)
        self.assertEqual(len(df.columns), 4)
        self.assertEqual(len(df), 3)

    #  The function exports only selected columns of the table if specific columns are selected.
    def test_export_selected_columns(self):
        # Arrange
        db_name = "test.db"
        table_name = "employees"
        output_filename = "output.csv"
        selected_columns = ["name", "age"]
    
        # Act
        export_to_csv(db_name, table_name, output_filename, selected_columns)
    
        # Assert
        # Check if the CSV file is created
        self.assertTrue(os.path.exists(output_filename))
        # Check if the CSV file contains the correct data
        df = pd.read_csv(output_filename)
        self.assertEqual(len(df.columns), 2)
        self.assertEqual(len(df), 3)

    #  The function raises an error if the given database name is invalid.
    def test_invalid_database_name(self):
        # Arrange
        db_name = "invalid.db"
        table_name = "employees"
        output_filename = "output.csv"
    
        # Act and Assert
        with self.assertRaises(sqlite3.OperationalError):
            export_to_csv(db_name, table_name, output_filename)

    #  The function raises an error if the given table name is invalid.
    def test_invalid_table_name(self):
        # Arrange
        db_name = "test.db"
        table_name = "invalid_table"
        output_filename = "output.csv"
    
        # Act and Assert
        with self.assertRaises(sqlite3.OperationalError):
            export_to_csv(db_name, table_name, output_filename)

    #  The function raises an error if the selected columns do not exist in the table.
    def test_invalid_selected_columns(self):
        # Arrange
        db_name = "test.db"
        table_name = "employees"
        output_filename = "output.csv"
        selected_columns = ["name", "invalid_column"]
    
        # Act and Assert
        with self.assertRaises(sqlite3.OperationalError):
            export_to_csv(db_name, table_name, output_filename, selected_columns)
