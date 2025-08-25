# 第四章 模型链
import warnings

warnings.filterwarnings("ignore")
from langchain_openai import ChatOpenAI  # type: ignore
from langchain.prompts import ChatPromptTemplate  # type: ignore
from langchain.chains import LLMChain, SimpleSequentialChain  # type: ignore
from tool import get_openai_key

api_key = get_openai_key()

# 这里我们将参数temperature设置为0.0，从而减少生成答案的随机性。
# 如果你想要每次得到不一样的有新意的答案，可以尝试调整该参数。
llm = ChatOpenAI(
    model="deepseek-reasoner",
    api_key=api_key,
    base_url="https://api.deepseek.com",
    temperature=0.0,
)

# prompt = ChatPromptTemplate.from_template(
#     "描述制造{product}的一个公司的最佳名称是什么?"
# )
# chain = LLMChain(llm=llm, prompt=prompt)
# product = "大号床单套装"
# res = chain.run(product)
# print(res)

# 提示模板 1 ：这个提示将接受产品并返回最佳名称来描述该公司
# first_prompt = ChatPromptTemplate.from_template(
#     "描述制造{product}的一个公司的最好的名称是什么"
# )
# chain_one = LLMChain(llm=llm, prompt=first_prompt)
# # 提示模板 2 ：接受公司名称，然后输出该公司的长为20个单词的描述
# second_prompt = ChatPromptTemplate.from_template(
#     "写一个20字的描述对于下面这个\
# 公司：{company_name}的"
# )
# chain_two = LLMChain(llm=llm, prompt=second_prompt)
# overall_simple_chain = SimpleSequentialChain(
#     chains=[chain_one, chain_two], verbose=True
# )

# product = "大号床单套装"
# res = overall_simple_chain.run(product)
# print(res)

# 三、顺序链