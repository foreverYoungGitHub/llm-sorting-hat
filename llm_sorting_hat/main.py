"""
This file demonstrates the example usage of guided decoding
of grammar, which mainly inspired by
https://github.com/vllm-project/vllm/blob/main/examples/offline_inference/structured_outputs.py
"""

import argparse

from vllm import LLM, SamplingParams
from vllm.sampling_params import GuidedDecodingParams

# Guided decoding by Grammar
grammar = """
object ::= "{" name_entry "," age_entry "," house_entry "}"

name_entry ::= "\"name\"" ":" string
age_entry ::= "\"age\"" ":" number
house_entry ::= "\"house\"" ":" house

string ::= "\"" name_char+ "\""
name_char ::= letter | space

letter ::= "\u0041" ... "\u005a" | "\u0061" ... "\u007a" | "\u4e00" ... "\u9fff" | "\u3400" ... "\u4dbf"
space ::= " "

number ::= digit+ | space
digit ::= "0"..."9"

house ::= "\"" house_value "\""
house_value ::= "Gryffindor" | "Slytherin" | "Ravenclaw" | "Hufflepuff"
"""

guided_decoding_params_grammar = GuidedDecodingParams(grammar=grammar)
sampling_params_grammar = SamplingParams(guided_decoding=guided_decoding_params_grammar)
prompt_grammar = """你是一顶聪明又古老的分院帽。请根据以下巫师新生的自我介绍，将他们分到合适的霍格沃兹学院（Gryffindor、Slytherin、Ravenclaw、Hufflepuff）中。

请只输出如下格式JSON，不要解释。
{{
    "name": "string",
    "age": "string",
    "house": "string"
}}
当用户相关信息为空时，请输出空字符串。

输入信息如下：
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
    parser.add_argument("--model", type=str, default="Qwen/Qwen3-0.6B")
    args = parser.parse_args()
    main(args.model)
