# LLM Sorting Hat / LLM 分院帽

A magical sorting hat powered by LLM that helps sort students into their Hogwarts houses based on their characteristics.
一个由 LLM 驱动的魔法分院帽，可以根据学生的特点将他们分到合适的霍格沃兹学院。

## Features / 功能特点

- Bilingual interface (English/Chinese) / 双语界面（英文/中文）
- Powered by LLM for intelligent house sorting / 由 LLM 驱动的智能分院
- Structured output in JSON format / JSON 格式的结构化输出
- Customizable model selection / 可自定义模型选择

## Installation / 安装

### 1. Set Up Your Development Environment / 设置开发环境

First, create a repository on GitHub with the same name as this project, and then run the following commands:

```bash
make install
```

### 2. Enter the Virtual Environment / 进入虚拟环境

```bash
source .venv/bin/activate
```

### 3. Run the llm-sorting-hat / 运行分院帽

Basic usage / 基本用法：
```bash
make run
```

With custom model / 使用自定义模型：
```bash
python llm_sorting_hat/main.py --model "your-model-name"
```

## Usage / 使用方法

1. Run the program / 运行程序
2. Enter your introduction in either English or Chinese / 用英文或中文输入你的自我介绍
3. The sorting hat will analyze your characteristics and assign you to a house / 分院帽将分析你的特点并将你分到合适的学院

## Output Format / 输出格式

The program will output a JSON with the following structure / 程序将输出如下结构的 JSON：

```json
{
    "name": "string",
    "age": "string",
    "house": "string"
}
```

Where house can be one of: / 其中 house 可以是以下之一：
- Gryffindor / 格兰芬多
- Slytherin / 斯莱特林
- Ravenclaw / 拉文克劳
- Hufflepuff / 赫奇帕奇
