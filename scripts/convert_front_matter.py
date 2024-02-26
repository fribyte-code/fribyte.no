import re
import sys
import toml
import yaml  # Import the pyyaml module

def yaml_to_toml(yaml_str):
    # Regular expression pattern to match YAML front-matter
    yaml_pattern = r'^---\n(.*?)\n---\n(.*)$'

    # Extract YAML front-matter and content
    match = re.match(yaml_pattern, yaml_str, re.DOTALL)

    if match:
        yaml_data = match.group(1)
        content = match.group(2)

        # Parse YAML to a Python dictionary
        yaml_dict = yaml.safe_load(yaml_data)

        if yaml_dict:
            # Extract only the desired fields
            author = yaml_dict.get('author', '')
            date = yaml_dict.get('subtitle', '')
            title = yaml_dict.get('title', '')

            # Create a new dictionary with the desired fields
            toml_dict = {
                'author': author,
                'date': date,
                'title': title
            }

            # Convert the new dictionary to TOML string
            toml_str = toml.dumps(toml_dict)

            # Create the new front-matter using TOML format
            new_front_matter = '+++\n' + toml_str + '+++\n' + content
            return new_front_matter

    return None

def main():
    if len(sys.argv) != 2:
        print("Usage: python convert_front_matter.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]

    try:
        with open(input_file, 'r') as file:
            input_content = file.read()

        new_front_matter = yaml_to_toml(input_content)

        if new_front_matter:
            # Print the converted front-matter to the console
            print(new_front_matter)
        else:
            print("Failed to convert front-matter.")

    except FileNotFoundError:
        print(f"File not found: {input_file}")
        sys.exit(1)

if __name__ == "__main__":
    main()
