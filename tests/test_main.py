from llm_sorting_hat import main as llm_sorting_hat


def test_prompt_grammar():
    user_input = """Hello, my name is Hermione Granger,
and I'm a first-year student at Hogwarts, 11 years old.
I come from a Muggle family—my parents are dentists—but ever since I received my letter, I’ve been absolutely fascinated by the magical world.
Before arriving, I read all the required textbooks, including Hogwarts: A History and Standard Book of Spells.
I'm very excited to start my magical education and hope to make a meaningful contribution to whichever house I’m sorted into!"""
    prompt_grammar = llm_sorting_hat.prompt_grammar.format(user_input=user_input)
    print(prompt_grammar)
    assert (
        prompt_grammar
        == """You're a wise and ancient Sorting Hat. Based on the following self-introduction from a young wizard, assign them to the most appropriate Hogwarts house.

Please output only a JSON object in the following format — no explanation:
{
    "name": "string",
    "age": "int",
    "house": "string"
}

Here is the input information:
Hello, my name is Hermione Granger,
and I'm a first-year student at Hogwarts, 11 years old.
I come from a Muggle family—my parents are dentists—but ever since I received my letter, I’ve been absolutely fascinated by the magical world.
Before arriving, I read all the required textbooks, including Hogwarts: A History and Standard Book of Spells.
I'm very excited to start my magical education and hope to make a meaningful contribution to whichever house I’m sorted into!
"""
    )
