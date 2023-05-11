import openai
import json
from config import openai_api_key
from utils import extract_json_string

openai.api_key = openai_api_key

def generate_json_response(temp, role, prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": role},
            {"role": "user", "content": prompt},
        ],
        max_tokens=1000,
        n=1,
        stop=None,
        temperature=temp,
    )
    return response.choices[0].message['content']

def generate_cs_file_list(game_name, additional_details):
    json_response = generate_json_response(0.5, "You are a planner",
        "Provide a JSON-formatted list of required C# Unity scripts for the game '{}'. Each JSON object should have a 'file_name' and a 'description'.\nAdditional details:\n{}".format(game_name, additional_details))
    print(json_response)
    cs_file_list = json.loads(extract_json_string(json_response))
    return cs_file_list

def generate_broken_down_cs_file_list(cs_file_list):
    broken_down_cs_file_list = []
    for cs_file in cs_file_list:
        json_response = generate_json_response(0.5, "You are an expert in C# Unity scripts",
            "Provide a JSON-formatted list of the resulting scripts that break down for provided script '{}'. Each JSON object should have a 'file_name' and a 'description'.".format(cs_file['file_name'], cs_file['description']))
        print(json_response)
        broken_down_cs_files = json.loads(extract_json_string(json_response))
        broken_down_cs_file_list.extend(broken_down_cs_files)
    return broken_down_cs_file_list

def generate_implemented_cs(cs_file):
    json_response = generate_json_response(0.5, "You are an expert in C# Unity scripts",
        "Implement a unity script that provided information '{}'.".format(cs_file['file_name'], cs_file['description']))
    return json_response