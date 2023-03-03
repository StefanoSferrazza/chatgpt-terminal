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

If the prompt parameter is not provided, the interactive mode is started where all the request parameters will be the 
ones provided during the initial call. To exit the interactive mode you can either interrupt the process (ctrl+c) or
using one of the following keywords: "exit", "e", "quit", "q".

Example:
```
python main.py -e "text-davinci-003" -m 4096

Prompt:
-->Say hello world

Completion:
Hello World!

Prompt:
-->exit
```

To know more about the available parameters:
```
python main.py --help
```