def export_to_libreoffice_calc(db_name, table_name, output_filename, selected_columns=None):
    conn = sqlite3.connect(db_name)
    if selected_columns:
        columns = ', '.join(selected_columns)
        query = f"SELECT {columns} FROM {table_name}"
    else:
        query = f"SELECT * FROM {table_name}"
    df = pd.read_sql_query(query, conn)
    df.to_excel(output_filename, sheet_name='Sheet1', index=False)
    conn.close()
