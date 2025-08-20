from langchain_openai import ChatOpenAI  # type: ignore
from langchain_core.prompts import ChatPromptTemplate  # type: ignore
from langchain.output_parsers import ResponseSchema  # type: ignore
from langchain.output_parsers import StructuredOutputParser  # type: ignore
from tool import get_openai_key

api_key = get_openai_key()
chat = ChatOpenAI(
    model="deepseek-chat",
    api_key=api_key,
    base_url="https://api.deepseek.com",
    temperature=0.0,
)

customer_review = """\
这款吹叶机非常神奇。 它有四个设置：\
吹蜡烛、微风、风城、龙卷风。 \
两天后就到了，正好赶上我妻子的\
周年纪念礼物。 \
我想我的妻子会喜欢它到说不出话来。 \
到目前为止，我是唯一一个使用它的人，而且我一直\
每隔一天早上用它来清理草坪上的叶子。 \
它比其他吹叶机稍微贵一点，\
但我认为它的额外功能是值得的。
"""
# review_template = """\
# 对于以下文本，请从中提取以下信息：
# 礼物：该商品是作为礼物送给别人的吗？ \
# 如果是，则回答 是的；如果否或未知，则回答 不是。
# 交货天数：产品需要多少天\
# 到达？ 如果没有找到该信息，则输出-1。
# 价钱：提取有关价值或价格的任何句子，\
# 并将它们输出为逗号分隔的 Python 列表。
# 使用以下键将输出格式化为 JSON：
# 礼物
# 交货天数
# 价钱
# 文本: {text}
# """

# prompt_template = ChatPromptTemplate.from_template(review_template)
# print("提示模版：", prompt_template)
# messages = prompt_template.format_messages(text=customer_review)
# response = chat.invoke(messages)
# print("结果类型:", type(response.content))
# print("结果:", response.content)

review_template_2 = """\
对于以下文本，请从中提取以下信息：：
礼物：该商品是作为礼物送给别人的吗？
如果是，则回答 是的；如果否或未知，则回答 不是。
交货天数：产品到达需要多少天？ 如果没有找到该信息，则输出-1。
价钱：提取有关价值或价格的任何句子，并将它们输出为逗号分隔的 Python 列表。
文本: {text}
{format_instructions}
"""
prompt = ChatPromptTemplate.from_template(template=review_template_2)
gift_schema = ResponseSchema(
    name="礼物",
    description="这件物品是作为礼物送给别人的吗？\
如果是，则回答 是的，\
如果否或未知，则回答 不是。",
)
delivery_days_schema = ResponseSchema(
    name="交货天数",
    description="产品需要多少天才能到达？\
如果没有找到该信息，则输出-1。",
)
price_value_schema = ResponseSchema(
    name="价钱",
    description="提取有关价值或价格的任何句子，\
并将它们输出为逗号分隔的 Python 列表",
)
response_schemas = [gift_schema, delivery_days_schema, price_value_schema]
output_parser = StructuredOutputParser.from_response_schemas(response_schemas)
format_instructions = output_parser.get_format_instructions()
print("输出格式规定：", format_instructions)
messages = prompt.format_messages(
    text=customer_review, format_instructions=format_instructions
)
print("第一条客户消息:", messages[0].content)

response = chat.invoke(messages)
print("结果类型:", type(response.content))
print("结果:", response.content)
output_dict = output_parser.parse(response.content)
print("解析后的结果类型:", type(output_dict))
print("解析后的结果:", output_dict)

# 第三章 储存