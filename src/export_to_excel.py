def export_to_excel(db_name, table_name, output_filename, selected_columns=None):
    conn = sqlite3.connect(db_name)
    if selected_columns:
        columns = ', '.join(selected_columns)
        query = f"SELECT {columns} FROM {table_name}"
    else:
        query = f"SELECT * FROM {table_name}"
    df = pd.read_sql_query(query, conn)
    wb = Workbook()
    ws = wb.active
    for row in dataframe_to_rows(df, index=False, header=True):
        ws.append(row)
    wb.save(output_filename)
    conn.close()
