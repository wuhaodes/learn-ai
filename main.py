# 1.3 通过LLM生成测试用例
from langchain.evaluation.qa import QAGenerateChain  # type: ignore #导入QA生成链，它将接收文档，并从每个文档中创建一个问题答案对
from langchain.chat_models import ChatOpenAI  # type: ignore #openai模型
from langchain.document_loaders import CSVLoader  # type: ignore #文档加载器，采用csv格式存储
from langchain.chains import RetrievalQA  # type: ignore #检索QA链，在文档上进行检索
from langchain.vectorstores import DocArrayInMemorySearch  # type: ignore #向量存储
from langchain.indexes import VectorstoreIndexCreator  # type: ignore
from langchain_community.embeddings import OllamaEmbeddings  # type: ignore
from langchain.text_splitter import RecursiveCharacterTextSplitter  # type: ignore

# 下面是langchain.evaluation.qa.generate_prompt中的源码，在template的最后加上“请使用中文输出”
from langchain.output_parsers.regex import RegexParser  # type: ignore
from langchain.prompts import PromptTemplate  # type: ignore
from langchain.base_language import BaseLanguageModel  # type: ignore
from typing import Any
from tool import get_openai_key

template = """You are a teacher coming up with questions to ask on a quiz.
Given the following document, please generate a question and answer based on that
document.
Example Format:
<Begin Document>
...
<End Document>
QUESTION: question here
ANSWER: answer here
These questions should be detailed and be based explicitly on information in the
document. Begin!
<Begin Document>
{doc}
<End Document>
请使用中文输出
"""

output_parser = RegexParser(
    regex=r"QUESTION: (.*?)\nANSWER: (.*)", output_keys=["query", "answer"]
)
PROMPT = PromptTemplate(
    input_variables=["doc"], template=template, output_parser=output_parser
)


# 继承QAGenerateChain
class ChineseQAGenerateChain(QAGenerateChain):
    """LLM Chain specifically for generating examples for question answering."""

    @classmethod
    def from_llm(cls, llm: BaseLanguageModel, **kwargs: Any) -> QAGenerateChain:
        """Load QA Generate Chain from LLM."""
        return cls(llm=llm, prompt=PROMPT, **kwargs)


api_key = get_openai_key()

llm = ChatOpenAI(
    model="deepseek-reasoner",
    api_key=api_key,
    base_url="https://api.deepseek.com",
    temperature=0.0,
)

file = "./data/product_data.csv"
loader = CSVLoader(file_path=file)
data = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=50)
chunks = text_splitter.split_documents(data)
embedding = OllamaEmbeddings(model="nomic-embed-text")

index = VectorstoreIndexCreator(
    vectorstore_cls=DocArrayInMemorySearch, embedding=embedding
).from_loaders([loader])

qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=index.vectorstore.as_retriever(),
    verbose=True,
    chain_type_kwargs={"document_separator": "<<<<>>>>>"},
)

example_gen_chain = ChineseQAGenerateChain.from_llm(
    llm
)  # 通过传递chat open AI语言模型来创建这个链
new_examples = example_gen_chain.apply([{"doc": t} for t in data[:5]])

examples = [
    {"query": "高清电视机怎么进行护理？", "answer": "使用干布清洁。"},
    {"query": "旅行背包有内外袋吗？", "answer": "有。"},
]

examples += [v for item in new_examples for k, v in item.items()]
print(qa.run(examples[0]["query"]))

# 三、 通过LLM进行评估实例


# 写个临时内容占个位，明天补回来，最近工作的事比较闹心，破公司拖欠工资