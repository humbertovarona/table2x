import pytest

class TestExportToExcel:

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
    
        # Act
        export_to_excel(db_name, table_name, output_filename)
    
        # Assert
        df = pd.read_excel(output_filename)
        assert len(df) == 2
        assert list(df.columns) == ['id', 'name', 'age']
        assert list(df['name']) == ['John', 'Jane']
        assert list(df['age']) == [25, 30]
    
        # Clean up
        conn.close()
        os.remove(output_filename)

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
    
        # Act
        export_to_excel(db_name, table_name, output_filename)
    
        # Assert
        df = pd.read_excel(output_filename)
        assert len(df) == 2
        assert list(df.columns) == ['id', 'name', 'age']
        assert list(df['name']) == ['John', 'Jane']
        assert list(df['age']) == [25, 30]
    
        # Clean up
        conn.close()
        os.remove(output_filename)

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
    
        # Act
        export_to_excel(db_name, table_name, output_filename, selected_columns=['name'])
    
        # Assert
        df = pd.read_excel(output_filename)
        assert len(df) == 2
        assert list(df.columns) == ['name']
        assert list(df['name']) == ['John', 'Jane']
    
        # Clean up
        conn.close()
        os.remove(output_filename)

    #  The function raises an error if the database file does not exist.
    def test_database_file_not_exist(self):
        # Arrange
        db_name = "nonexistent.db"
        table_name = "test_table"
        output_filename = "output.xlsx"
    
        # Act and Assert
        with pytest.raises(sqlite3.OperationalError):
            export_to_excel(db_name, table_name, output_filename)

    #  The function raises an error if the table name does not exist in the database.
    def test_table_name_not_exist(self):
        # Arrange
        db_name = "test.db"
        table_name = "nonexistent_table"
        output_filename = "output.xlsx"
        conn = sqlite3.connect(db_name)
    
        # Act and Assert
        with pytest.raises(pd.io.sql.DatabaseError):
            export_to_excel(db_name, table_name, output_filename)
    
        # Clean up
        conn.close()

    #  The function raises an error if the selected columns do not exist in the table.
    def test_selected_columns_not_exist(self):
        # Arrange
        db_name = "test.db"
        table_name = "test_table"
        output_filename = "output.xlsx"
        conn = sqlite3.connect(db_name)
        conn.execute("CREATE TABLE test_table (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")
        conn.execute("INSERT INTO test_table (name, age) VALUES ('John', 25)")
        conn.execute("INSERT INTO test_table (name, age) VALUES ('Jane', 30)")
        conn.commit()
    
        # Act and Assert
        with pytest.raises(pd.io.sql.DatabaseError):
            export_to_excel(db_name, table_name, output_filename, selected_columns=['nonexistent_column'])
    
        # Clean up
        conn.close()
