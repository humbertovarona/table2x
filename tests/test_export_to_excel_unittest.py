import unittest

class TestExportToExcel(unittest.TestCase):

    #  The function exports data from a SQLite database to an Excel file.
    def test_export_all_columns(self):
        # Arrange
        db_name = "test.db"
        table_name = "test_table"
        output_filename = "output.xlsx"
        conn = sqlite3.connect(db_name)
        conn.execute("CREATE TABLE test_table (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")
        conn.execute("INSERT INTO test_table (name, age) VALUES ('John', 25)")
        conn.execute("INSERT INTO test_table (name, age) VALUES ('Jane', 30)")
        conn.commit()
        conn.close()

        # Act
        export_to_excel(db_name, table_name, output_filename)

        # Assert
        df = pd.read_excel(output_filename)
        expected_columns = ['id', 'name', 'age']
        self.assertListEqual(list(df.columns), expected_columns)
        expected_data = [(1, 'John', 25), (2, 'Jane', 30)]
        self.assertListEqual(list(df.itertuples(index=False, name=None)), expected_data)

    #  The function exports all columns if no specific columns are selected.
    def test_export_all_columns_no_selection(self):
        # Arrange
        db_name = "test.db"
        table_name = "test_table"
        output_filename = "output.xlsx"
        conn = sqlite3.connect(db_name)
        conn.execute("CREATE TABLE test_table (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")
        conn.execute("INSERT INTO test_table (name, age) VALUES ('John', 25)")
        conn.execute("INSERT INTO test_table (name, age) VALUES ('Jane', 30)")
        conn.commit()
        conn.close()

        # Act
        export_to_excel(db_name, table_name, output_filename)

        # Assert
        df = pd.read_excel(output_filename)
        expected_columns = ['id', 'name', 'age']
        self.assertListEqual(list(df.columns), expected_columns)
        expected_data = [(1, 'John', 25), (2, 'Jane', 30)]
        self.assertListEqual(list(df.itertuples(index=False, name=None)), expected_data)

    #  The function exports only selected columns if specified.
    def test_export_selected_columns(self):
        # Arrange
        db_name = "test.db"
        table_name = "test_table"
        output_filename = "output.xlsx"
        conn = sqlite3.connect(db_name)
        conn.execute("CREATE TABLE test_table (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")
        conn.execute("INSERT INTO test_table (name, age) VALUES ('John', 25)")
        conn.execute("INSERT INTO test_table (name, age) VALUES ('Jane', 30)")
        conn.commit()
        conn.close()

        # Act
        export_to_excel(db_name, table_name, output_filename, selected_columns=['name', 'age'])

        # Assert
        df = pd.read_excel(output_filename)
        expected_columns = ['name', 'age']
        self.assertListEqual(list(df.columns), expected_columns)
        expected_data = [('John', 25), ('Jane', 30)]
        self.assertListEqual(list(df.itertuples(index=False, name=None)), expected_data)

    #  The function raises an error if the database file does not exist.
    def test_database_file_not_exist(self):
        # Arrange
        db_name = "nonexistent.db"
        table_name = "test_table"
        output_filename = "output.xlsx"

        # Act and Assert
        with self.assertRaises(sqlite3.OperationalError):
            export_to_excel(db_name, table_name, output_filename)

    #  The function raises an error if the table name does not exist in the database.
    def test_table_name_not_exist(self):
        # Arrange
        db_name = "test.db"
        table_name = "nonexistent_table"
        output_filename = "output.xlsx"
        conn = sqlite3.connect(db_name)
        conn.execute("CREATE TABLE test_table (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")
        conn.commit()
        conn.close()

        # Act and Assert
        with self.assertRaises(sqlite3.OperationalError):
            export_to_excel(db_name, table_name, output_filename)

    #  The function raises an error if the selected columns do not exist in the table.
    def test_selected_columns_not_exist(self):
        # Arrange
        db_name = "test.db"
        table_name = "test_table"
        output_filename = "output.xlsx"
        conn = sqlite3.connect(db_name)
        conn.execute("CREATE TABLE test_table (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")
        conn.commit()
        conn.close()

        # Act and Assert
        with self.assertRaises(sqlite3.OperationalError):
            export_to_excel(db_name, table_name, output_filename, selected_columns=['nonexistent_column'])
