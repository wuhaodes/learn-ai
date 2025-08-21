import asyncio
from langchain_openai import ChatOpenAI  # type: ignore
from langchain.memory import ConversationBufferMemory  # type: ignore
from langchain_core.prompts import ChatPromptTemplate  # type: ignore
from langchain_core.prompts.chat import (  # type: ignore
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
)
from tool import get_openai_key

api_key = get_openai_key()
# chat = ChatOpenAI(
#     model="deepseek-chat",
#     api_key=api_key,
#     base_url="https://api.deepseek.com",
#     temperature=0.0,
# )

# 第三章 储存
# 这里我们将参数temperature设置为0.0，从而减少生成答案的随机性。
# 如果你想要每次得到不一样的有新意的答案，可以尝试增大该参数。
llm = ChatOpenAI(
    model="deepseek-chat",
    api_key=api_key,
    base_url="https://api.deepseek.com",
    temperature=0.0,
)
# conversation = ConversationChain(llm=llm, memory = memory, verbose=True )
# conversation.predict(input="你好, 我叫吴昊")
# conversation.predict(input="1+1等于多少？")
# conversation.predict(input="我叫什么名字？")
# res = conversation.predict(input="结束对话")
# print(res)
# # print(memory.buffer)
# # print(memory.load_memory_variables({}))

# prompt = ChatPromptTemplate(
#     [
#         MessagesPlaceholder(variable_name="chat_history"),
#         HumanMessagePromptTemplate.from_template("{text}"),
#     ]
# )

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=False)
memory.save_context(
    {"input": "你好，我叫吴昊"}, {"output": "你好啊，我是小优,优管公司的智能机器人"}
)
memory.load_memory_variables({})
memory.save_context(
    {"input": "很高兴和你成为朋友！"}, {"output": "是的，让我们一起去冒险吧！"}
)

prompt = ChatPromptTemplate(
    [
        MessagesPlaceholder(variable_name="chat_history"),
        HumanMessagePromptTemplate.from_template("{text}"),
    ]
)

chain = prompt | llm

messages = memory.buffer_as_messages

res = chain.invoke({"text": "首站目的地上海", "chat_history": messages})

print(f"\n小优: {res.content}")

# 2.2 在对话链中应用窗口储存