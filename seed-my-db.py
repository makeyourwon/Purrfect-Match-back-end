import json

def generate_sql_from_json(json_file_path):
    with open(json_file_path, 'r') as file:
        data = json.load(file)
    
    sql_statements = []

    for item in data:

        sql = f"""
INSERT INTO animal (name, type, breed, age, size, gender, color, status, location, description, photos, contact)
VALUES (
    '{item["name"]}',
    '{item["type"]}',
    '{json.dumps(item["breed"])}',  
    '{item["age"]}',
    '{item["size"]}',
    '{item["gender"]}',
    '{json.dumps(item["color"])}',  
    '{item["status"]}',
    '{item["location"]}',
    {f"'{item["description"].replace("'", "''")}'" if item["description"] else 'NULL'},  
    '{json.dumps(item["photos"])}',  
    '{json.dumps(item["contact"])}' 
);"""
        sql_statements.append(sql)
    
    return sql_statements

json_file_path = 'transformed_data_output.json'
sql_statements = generate_sql_from_json(json_file_path)

with open('seed_database.sql', 'w') as f:
    for statement in sql_statements:
        f.write(statement + "\n\n")
