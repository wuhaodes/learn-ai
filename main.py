from langchain_openai import ChatOpenAI  # type: ignore
from langchain_core.prompts import ChatPromptTemplate  # type: ignore
from tool import get_openai_key

api_key = get_openai_key()
chat = ChatOpenAI(
    model="deepseek-chat",
    api_key=api_key,
    base_url="https://api.deepseek.com",
    temperature=0.0,
)
print(chat)

# 首先，构造一个提示模版字符串：`template_string`
template_string = """把由三个反引号分隔的文本\
翻译成一种{style}风格。\
文本: ```{text}```
"""
# 然后，我们调用`ChatPromptTemplatee.from_template()`函数将
# 上面的提示模版字符`template_string`转换为提示模版`prompt_template`

prompt_template = ChatPromptTemplate.from_template(template_string)
print("\n", prompt_template.messages[0].prompt)

customer_style = """正式普通话 \
用一个平静、尊敬的语气
"""
customer_email = """
嗯呐，我现在可是火冒三丈，我那个搅拌机盖子竟然飞了出去，把我厨房的墙壁都溅上了果汁！
更糟糕的是，保修条款可不包括清理我厨房的费用。
伙计，赶紧给我过来！
"""

# 使用提示模版
customer_messages = prompt_template.format_messages(
    style=customer_style, text=customer_email
)
# 打印客户消息类型
print("客户消息类型:", type(customer_messages), "\n")
# 打印第一个客户消息类型
print("第一个客户客户消息类型类型:", type(customer_messages[0]), "\n")
# 打印第一个元素
print("第一个客户客户消息类型类型: ", customer_messages[0], "\n")
customer_response = chat.invoke(customer_messages)
print(customer_response.content)

service_reply = """嘿，顾客， \
保修不包括厨房的清洁费用， \
因为您在启动搅拌机之前 \
忘记盖上盖子而误用搅拌机, \
这是您的错。 \
倒霉！ 再见！
"""
service_style_pirate = """\
一个有礼貌的语气 \
使用海盗风格\
"""
service_messages = prompt_template.format_messages(
    style=service_style_pirate, text=service_reply
)
print("\n", service_messages[0].content)

service_response = chat.invoke(service_messages)
print(service_response.content)

# 2.2.3 为什么需要提示模版