import re
import os

def extract_json_string(text):
    code_block_pattern = re.compile(r"```\n(.*?)\n```", re.DOTALL)
    match = code_block_pattern.search(text)
    if match:
        return match.group(1)
    else:
        code_block_pattern = re.compile(r"```json\n(.*?)\n```", re.DOTALL)
        match = code_block_pattern.search(text)
        if match:
            return match.group(1)
        else:
            return text

def get_user_input(prompt):
    print(">>")
    print(prompt)

    user_input = ""
    try:
        while True:
            line = input()
            if not line:
                break
            user_input += line + "\n"
    except (EOFError, KeyboardInterrupt):
        print("Responding...\n")

    return user_input.strip()

def print_cs_file_list(cs_file_list, title):
    print(title)
    for cs_file in cs_file_list:
        print("File Name: {}, Description: {}".format(cs_file['file_name'], cs_file['description']))
    print()

def extract_code_blocks_and_save(text, GAME_NAME):
    def extract_class_name(text):
        class_pattern = re.compile(r"public class (\w+)")
        match = class_pattern.search(text)
        if match:
            return match.group(1)
        else:
            return None
    try:
        code_block_pattern = re.compile(r"```\n(.*?)\n```", re.DOTALL)
        code_blocks = code_block_pattern.findall(text)
        for i, code_block in enumerate(code_blocks, start=1):
            directory_name = GAME_NAME.replace("\n", "")
            if not os.path.exists(directory_name):
                os.makedirs(directory_name)
            with open(directory_name + "/" + extract_class_name(code_block)+".cs", "w") as file:
                file.write(code_block)
                print("Code Generated!: " + extract_class_name(code_block)+".cs\n")
    except Exception as e:
        print(e)