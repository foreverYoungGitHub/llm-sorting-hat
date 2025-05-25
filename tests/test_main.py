from llm_sorting_hat import main as llm_sorting_hat


def test_prompt_grammar():
    user_input = "我叫哈利·波特，今年11岁，来自伦敦。我是一个勇敢、聪明、有正义感的小巫师。"
    prompt_grammar = llm_sorting_hat.prompt_grammar.format(user_input=user_input)
    assert (
        prompt_grammar
        == """你是一顶聪明又古老的分院帽。请根据以下巫师新生的自我介绍，将他们分到合适的霍格沃兹学院（Gryffindor、Slytherin、Ravenclaw、Hufflepuff）中。

请只输出如下格式JSON，不要解释。
{
    "name": "string",
    "age": "string",
    "house": "string"
}
当用户相关信息为空时，请输出空字符串。

输入信息如下：
我叫哈利·波特，今年11岁，来自伦敦。我是一个勇敢、聪明、有正义感的小巫师。
"""
    )
