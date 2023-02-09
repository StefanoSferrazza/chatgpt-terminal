# chatgpt-terminal
This is a simple terminal tool to send a prompt through the chatGPT API

## Usage
Dependencies can be installed though `pipenv install` or manually, by checking them in [Pipfile](./Pipfile).

It is required to set an evironment variable containg the openAI API key:
```
export OPENAI_API_KEY=...
```

Example:
```
python main.py -p "Reply with \"Hello World\""
```

To know more usage parameters:
```
python main.py --help
```