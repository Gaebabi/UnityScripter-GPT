from gpt import generate_cs_file_list, generate_broken_down_cs_file_list, generate_implemented_cs
from utils import get_user_input, print_cs_file_list, extract_code_blocks_and_save

if __name__ == '__main__':
    while True:
        game_name = get_user_input("Enter your game name (press Ctrl+Z followed by Enter to finish input):")
        if not game_name:
            print("No input received. Exiting...")
            break

        additional_details = get_user_input("Additional details (press Ctrl+Z followed by Enter to finish input):")
        if not additional_details:
            print("No input received. Exiting...")
            break

        # Generate JSON output from GPT
        cs_file_list = generate_cs_file_list(game_name, additional_details)
        print_cs_file_list(cs_file_list, "C# File List:")
        
        # Iterate through the cs_file_list and break down each element into smaller scripts
        broken_down_cs_file_list = generate_broken_down_cs_file_list(cs_file_list)
        print_cs_file_list(broken_down_cs_file_list, "Broken Down C# File List:")

        # C# List to make real cs files in game_name directory
        for cs_file in broken_down_cs_file_list:
            implementation = generate_implemented_cs(cs_file)
            print(implementation)
            extract_code_blocks_and_save(implementation, game_name)

    print("Exiting the program...")
