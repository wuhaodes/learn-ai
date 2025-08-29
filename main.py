# 第六章 评估
from langchain.chains import RetrievalQA  # type: ignore #检索QA链，在文档上进行检索
from langchain.chat_models import ChatOpenAI  # type: ignore #openai模型
from langchain.document_loaders import CSVLoader  # type: ignore #文档加载器，采用csv格式存储
from langchain.indexes import VectorstoreIndexCreator  # type: ignore #导入向量存储索引创建器
from langchain.vectorstores import DocArrayInMemorySearch  # type: ignore #向量存储
from langchain_community.embeddings import OllamaEmbeddings  # type: ignore
from langchain.text_splitter import RecursiveCharacterTextSplitter  # type: ignore
from tool import get_openai_key
import ollama  # type: ignore
import pandas as pd

file = "./data/product_data.csv"
loader = CSVLoader(file_path=file)
data = loader.load()


# 查看数据
# test_data = pd.read_csv(file, skiprows=0)
# table_data = test_data.head()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=50)
chunks = text_splitter.split_documents(data)
embedding = OllamaEmbeddings(model="nomic-embed-text")

index = VectorstoreIndexCreator(
    vectorstore_cls=DocArrayInMemorySearch,
    embedding=embedding,
).from_loaders([loader])

api_key = get_openai_key()

llm = ChatOpenAI(
    model="deepseek-reasoner",
    api_key=api_key,
    base_url="https://api.deepseek.com",
    temperature=0.0,
)

qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=index.vectorstore.as_retriever(),
    verbose=True,
    chain_type_kwargs={"document_separator": "<<<<>>>>>"},
)

# print(data[10])
# print(data[11])


examples = [
    {"query": "高清电视机怎么进行护理？", "answer": "使用干布清洁。"},
    {"query": "旅行背包有内外袋吗？", "answer": "有。"},
]

# 1.3 通过LLM生成测试用例