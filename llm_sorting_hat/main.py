"""
This file demonstrates the example usage of guided decoding
of grammar, which mainly inspired by
https://github.com/vllm-project/vllm/blob/main/examples/offline_inference/structured_outputs.py
"""

import argparse

from vllm import LLM, SamplingParams
from vllm.sampling_params import GuidedDecodingParams

# Guided decoding by Grammar
grammar = r"""root ::= "{" name_entry "," age_entry "," house_entry "}"

name_entry ::= (([\"] "name" [\"])) ":" basic_string
age_entry ::= (([\"] "age" [\"])) ":" age_value
house_entry ::= (([\"] "house" [\"])) ":" house_string

age_value ::= ("0" | [1-9] [0-9]*)
house_string ::= (([\"] house_value [\"]))
house_value ::= "Gryffindor" | "Slytherin" | "Ravenclaw" | "Hufflepuff"

basic_string ::= (([\"] basic_string_1 [\"]))
basic_string_1 ::= "" | [^"\\\x00-\x1F] basic_string_1 | "\\" escape basic_string_1
escape ::= ["\\/bfnrt] | "u" [A-Fa-f0-9] [A-Fa-f0-9] [A-Fa-f0-9] [A-Fa-f0-9]
"""

guided_decoding_params_grammar = GuidedDecodingParams(grammar=grammar)
sampling_params_grammar = SamplingParams(
    guided_decoding=guided_decoding_params_grammar, max_tokens=100, temperature=0.1
)
prompt_grammar = """You're a wise and ancient Sorting Hat. Based on the following self-introduction from a young wizard, assign them to the most appropriate Hogwarts house.

Please output only a JSON object in the following format — no explanation:
{{
    "name": "string",
    "age": "int",
    "house": "string"
}}

Here is the input information:
{user_input}
"""


def generate_output(prompt: str, sampling_params: SamplingParams, llm: LLM) -> str:
    outputs = llm.generate(prompts=prompt, sampling_params=sampling_params)
    return outputs[0].outputs[0].text


def get_user_input() -> str:
    """Collect user information"""
    print("\nPlease introduce yourself / 请介绍一下自己:")
    return input().strip()


def main(model: str) -> None:
    # Get user input first
    user_input = get_user_input()
    user_prompt = prompt_grammar.format(user_input=user_input)

    # Initialize LLM
    llm = LLM(model=model, max_model_len=100)

    grammar_output = generate_output(user_prompt, sampling_params_grammar, llm)
    print(grammar_output)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", type=str, default="meta-llama/Llama-3.2-1B-Instruct")
    args = parser.parse_args()
    main(args.model)
