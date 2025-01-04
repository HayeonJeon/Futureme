import json
import openai

def dd_generate_gpt4_basic(system_prompt, knowledge, user_prompt):
    completion = openai.chat.completions.create(
        model = 'gpt-4o',
        messages = [
            {'role': 'system', 'content': system_prompt},
            {"role": "assistant", "content": knowledge},
            {'role': 'user', 'content': user_prompt}
        ]
    )
    return completion.choices[0].message.content

def pvq_summary_gpt4(summary):
    system_lib_file = './data/prompt_template/PVQ_summary_sys.txt'
    f = open(system_lib_file, "r")
    sys_prompt = f.read()
    f.close()
    completion = openai.chat.completions.create(
        model = 'gpt-4o',
        messages = [
            {'role': 'system', 'content': sys_prompt},
            {'role': 'user', 'content': summary}
        ]
    )
    return completion.choices[0].message.content

def bfi_summary_gpt4(summary):
    system_lib_file = './data/prompt_template/BFI_summary_sys.txt'
    f = open(system_lib_file, "r")
    sys_prompt = f.read()
    f.close()
    completion = openai.chat.completions.create(
        model = 'gpt-4o',
        messages = [
            {'role': 'system', 'content': sys_prompt},
            {'role': 'user', 'content': summary}
        ]
    )
    return completion.choices[0].message.content