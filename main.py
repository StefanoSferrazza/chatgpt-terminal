import argparse
import openai
import os
from transformers import GPT2TokenizerFast

tokens_limit = 4096


def cap_tokens(prompt, max_tokens):
    global tokens_limit
    os.environ["TOKENIZERS_PARALLELISM"]="true"
    tokenizer = GPT2TokenizerFast.from_pretrained("gpt2")
    prompt_tokens = len(tokenizer(prompt)['input_ids'])
    allowed_tokens = tokens_limit - prompt_tokens - 1
    if max_tokens > allowed_tokens:
        return allowed_tokens
    else:
        return max_tokens


def update_tokens_limit(model_name):
    global tokens_limit
    if model_name != "text-davinci-003":
        tokens_limit = 2048


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--prompt',
                        help=f'Prompt to send to chatGPT',
                        default=None)
    parser.add_argument('-e', '--engine',
                        help='Chatgpt engine to be used. Default is set to \'text-davinci-003\'. To see a complete '
                             'list of available models, use the utility \'print_models.py\'.',
                        default="text-davinci-003")
    parser.add_argument('-t', '--temperature',
                        help='What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the '
                             'output more random, while lower values like 0.2 will make it more focused and '
                             'deterministic. We generally recommend altering this or top_p but not both',
                        default=0.0)
    parser.add_argument('-m', '--max_tokens',
                        help='Maximum number of tokens to be used in the answer. Maximum amount of tokens is 2048 for '
                             'older models, 4096 for newer. Only if \'text-davinci-003\' is selected will be allowed '
                             'the limit of 4096.',
                        default=256)
    parser.add_argument('-top', '--top_p',
                        help='An alternative to sampling with temperature, called nucleus sampling, where the model '
                             'considers the results of the tokens with the indicated probability mass. So 0.1 means '
                             'only the tokens comprising the top 10 percent probability mass are considered. '
                             'We generally recommend altering this or temperature but not both.',
                        default=0.1)
    parser.add_argument('-f', '--frequency_penalty',
                        help="Number between -2.0 and 2.0. Positive values penalize new tokens based on their "
                             "existing frequency in the text so far, decreasing the model's likelihood to repeat the "
                             "same line verbatim.",
                        default=0.0)
    parser.add_argument('-pres', '--presence_penalty',
                        help="Number between -2.0 and 2.0. Positive values penalize new tokens based on whether they "
                             "appear in the text so far, increasing the model's likelihood to talk about new topics.",
                        default=0.0)
    parser.add_argument('-o', '--output',
                        help='Output file path where the answer should be stored. If not specified, the answer will '
                             'be printed in the terminal. Example: ./resources/one_off_output.txt',
                        default=None)
    args = parser.parse_args()
    openai.api_key = os.getenv("OPENAI_API_KEY")
    update_tokens_limit(args.engine)
    if args.prompt is None:
        max_tokens = cap_tokens("X"*500, int(args.max_tokens))
    else:
        max_tokens = cap_tokens(args.prompt, int(args.max_tokens))
    if args.prompt != None:
        response = openai.Completion.create(
            engine=args.engine,
            prompt=args.prompt,
            temperature=float(args.temperature),
            max_tokens=max_tokens,
            top_p=float(args.top_p),
            frequency_penalty=float(args.frequency_penalty),
            presence_penalty=float(args.presence_penalty)
        )
        response_text = response['choices'][0]['text'].replace("\n", "")
        if args.output == None:
            print(response_text)
        else:
            with open(args.output, "w") as output_file:
                output_file.write(response_text)
    else:
        while True:
            prompt = input("\nPrompt:\n-->")
            if prompt == "exit" or prompt == "e" or prompt == "quit" or prompt == "q":
                break
            response = openai.Completion.create(
                        engine=args.engine,
                        prompt=prompt,
                        temperature=float(args.temperature),
                        max_tokens=max_tokens,
                        top_p=float(args.top_p),
                        frequency_penalty=float(args.frequency_penalty),
                        presence_penalty=float(args.presence_penalty)
                    )
            response_text = response['choices'][0]['text'].replace("\n", "")
            print("\nCompletion:\n" + response_text + "\n")