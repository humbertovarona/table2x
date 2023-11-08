def export_to_latex(db_name, table_name, output_filename, selected_columns=None):
    conn = sqlite3.connect(db_name)
    if selected_columns:
        columns = ', '.join(selected_columns)
        query = f"SELECT {columns} FROM {table_name}"
    else:
        query = f"SELECT * FROM {table_name}"
    df = pd.read_sql_query(query, conn)
    latex_table = df.to_latex(index=False)
    with open(output_filename, 'w') as latex_file:
        latex_file.write(latex_table)
    conn.close()
