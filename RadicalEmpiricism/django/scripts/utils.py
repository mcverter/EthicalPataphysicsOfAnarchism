import os
def open_file_relative_to_scripts_dir(relative_path):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(dir_path, relative_path)

def update_sql_command(table, setFieldName, setFieldValue, whereFieldName, whereFieldValue):
    output = f"UPDATE WordAnalysis_word SET {setFieldName} = '{setFieldValue}' WHERE {whereFieldName}='{whereFieldValue}';\n"

