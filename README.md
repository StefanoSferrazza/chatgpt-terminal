# chatgpt-terminal
This is a simple terminal tool to send a prompt through the chatGPT API

## Usage
Dependencies can be installed though `pipenv install` or manually, by checking them in [Pipfile](./Pipfile).

Activate the python environment with `pipenv shell`.

Set an environment variable containing the openAI API key:
```
export OPENAI_API_KEY=...
```

Example of minimum usage:
```
python main.py -p "Reply with \"Hello World\""
```

To know more about the available parameters:
```
python main.py --help
```