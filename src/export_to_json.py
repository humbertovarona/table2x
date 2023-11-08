def export_to_json(db_name, table_name, output_filename, selected_columns=None):
    conn = sqlite3.connect(db_name)
    if selected_columns:
        columns = ', '.join(selected_columns)
        query = f"SELECT {columns} FROM {table_name}"
    else:
        query = f"SELECT * FROM {table_name}"
    df = pd.read_sql_query(query, conn)
    json_data = df.to_json(orient="records", indent=4)
    with open(json_filename, 'w') as json_file:
        json_file.write(output_filename)
    conn.close()
