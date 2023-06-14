import gradio
from src.proxy import chat

# 左边是介绍、聊天记录，右边是对话框

dd_prompt = '''下面是一个数字分身{name}的性格、介绍：
  {desc}
下面是数字分身和别人的对话：
  {chat}
请针对上文，扮演这个数字分身，和我聊天，接下来你会和我说：'''

# 哆啦A梦

# 哆啦A梦，有各种各样的道具，喜欢帮助别人，喜欢吃铜锣烧

# 哆啦A梦：大雄，你怎么又闯祸了！！！

def dd_chat(dd_name, dd_desc, dd_example_chat, msg, his):
    dd_soul = dd_prompt.format(name=dd_name, desc=dd_desc, chat=dd_example_chat)
    _his = [[dd_soul, ''], *his]
    _res = chat(msg, _his)
    his.append([msg, _res])
    return '', his 

# 用一个小故事来测试性格

# 人物介绍

# 聊天记录

# 基于性格、聊天记录来对话

import gradio as gr
import os
import random
import time

with gr.Blocks() as demo:
    gr.Markdown("Start typing below and then click **Run** to see the output.")
    with gr.Row():
        with gr.Column():
            dd_name = gr.Textbox(placeholder="昵称", lines=1)
            dd_desc = gr.Textbox(placeholder="介绍一下你想做的分身，比如性格、爱好、职业、梦想、年龄等等", lines=5)
            dd_example_chat = gr.Textbox(placeholder="输入分身语录，或和别人的对话", lines=10)
        
        with gr.Column():
            chatbot = gr.Chatbot(lines=10, placeholder="和分身聊天", live=True)
            msg = gr.Textbox()
            with gr.Row():
                chat_btn = gr.Button("Chat")
                clear = gr.Button("Clear")
        chat_btn.click(dd_chat, [dd_name, dd_desc, dd_example_chat, msg, chatbot], [msg, chatbot])
        msg.submit(dd_chat, [dd_name, dd_desc, dd_example_chat, msg, chatbot], [msg, chatbot])
    gr.Examples(inputs=[dd_name, dd_desc, dd_example_chat], examples=[['哆啦A梦', '哆啦A梦，有各种各样的道具，喜欢帮助别人，喜欢吃铜锣烧', '哆啦A梦：大雄，你怎么又闯祸了！！！']])
    # btn = gr.Button("Run")
    # btn.click(fn=update, inputs=inp, outputs=out)

if __name__ == '__main__':
    demo.launch()
