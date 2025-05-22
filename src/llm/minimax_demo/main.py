# coding=utf-8
import dashscope

messages = [{'role': 'system', 'content': 'You are a helpful assistant.'},
            {'role': 'user', 'content': 'Who are you?'}]
response = dashscope.Generation.call(
    model='abab6.5s-chat',
    messages=messages,
)
print(response)
