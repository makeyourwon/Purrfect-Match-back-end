import json

def load_json_file(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)

def transform_data(raw_json_list):
    transformed_data = []

    # print(type(raw_json_list))


    for item in raw_json_list:
        print(item) 
        transformed_object = {
            "name": item["name"],
            "type": item["type"],
            "breed": {
                "primary": item["breeds"]["primary"],
                "secondary": item["breeds"]["secondary"],
                "mixed": item["breeds"]["mixed"],
                "unknown": item["breeds"]["unknown"],
            },
            "age": item["age"],
            "size": item["size"],
            "gender": item["gender"],
            "color": {  
                "primary": item["colors"]["primary"] if item["colors"]["primary"] else None,
                "secondary": item["colors"]["secondary"] if item["colors"]["secondary"] else None,
                "tertiary": item["colors"]["tertiary"] if item["colors"]["tertiary"] else None,
            },
            "status": item["status"],
            "location": "{}, {}, {} {}".format(
                item["contact"]["address"]["address1"],
                item["contact"]["address"]["city"],
                item["contact"]["address"]["state"],
                item["contact"]["address"]["postcode"],
            ),
            "description": item["description"],
            "photos": item["photos"],  
            "contact": {
                "email": item["contact"]["email"],
                "phone": item["contact"]["phone"],
                "address": item["contact"]["address"],
            },
        }
        transformed_data.append(transformed_object)
    
    return transformed_data

# Path to your pet-seed.json file
file_path = 'pet-seed.json'

# Load JSON data from the file
raw_data = load_json_file(file_path)

# Transform the raw JSON data
transformed_data = transform_data(raw_data)

# Optionally, to print or save the transformed data
print(json.dumps(transformed_data, indent=4))
with open('transformed_data_output.json', 'w') as f:
    json.dump(transformed_data, f, indent=4)
