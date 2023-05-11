# 🎮 UnityScripter-GPT 🧠
Generator Unity C# scripts with GPT for your prototype project

## 🚀 Features

- 📋 Generate a JSON-formatted list of required C# Unity scripts.
- 🔍 Breakdown of each script into smaller scripts.
- 🙌 Automatically generate C# script files.

## ⚙️ Installation

This project requires Python 3.6+ and pip. After cloning the repository, run the following command to install the required libraries:

```bash
pip install -r requirements.txt
```

## 🕹️ Usage

This project uses the OpenAI API, and requires an API key. Follow these steps to set up your API key:

1. [Sign up](https://beta.openai.com/signup/) for an account with OpenAI to get an API key.

2. Create a new file in the root directory of this project named `.env`.

3. Open the `.env` file with a text editor, and add the following line, replacing `your_api_key` with your actual OpenAI API key:

```txt
OPENAI_API_KEY=your_api_key
```

4. Save and close the `.env` file.

Remember to add `.env` to your `.gitignore` file to ensure that you don't accidentally commit your API key to version control. It's also important to keep your API key secret, as anyone with access to it could make requests to the OpenAI API on your behalf and potentially incur costs.

Once your API key is set up, you can run the script using Python:

```bash
python main.py
```

When prompted, enter your game name and any additional details. The script will then generate a list of required C# Unity scripts and a breakdown of each script.

## 👥 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## License
This project is licensed under the terms of the MIT license.
