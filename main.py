# 第五章 基于文档的问答
# from langchain.chains import RetrievalQA  # type: ignore #检索QA链，在文档上进行检索
# from langchain.chat_models import ChatOpenAI  # type: ignore #openai模型
# from langchain.document_loaders import CSVLoader  # type: ignore #文档加载器，采用csv格式存储
# from langchain.vectorstores import DocArrayInMemorySearch  # type: ignore #向量存储
# from IPython.display import display, Markdown  # type: ignore #在jupyter显示信息的工具
# from langchain.indexes import VectorstoreIndexCreator  # type: ignore
# from langchain.embeddings import OpenAIEmbeddings  # type: ignore
# from tool import get_openai_key
# import ollama  # type: ignore
# import pandas as pd

# key = get_openai_key()

# file = "./data/OutdoorClothingCatalog_1000.csv"
# # 使用langchain文档加载器对数据进行导入
# loader = CSVLoader(file_path=file)
# # 使用pandas导入数据，用以查看
# data = pd.read_csv(file, usecols=[1, 2])
# doc = data.head()
# print(doc)

# # 创建 embedding 实例
# embedding = ollama.embed(model="nomic-embed-text", input=doc)

# # 导入向量存储索引创建器
# # 创建指定向量存储类, 创建完成后，从加载器中调用, 通过文档加载器列表加载
# index = VectorstoreIndexCreator(
#     vectorstore_cls=DocArrayInMemorySearch, embedding=embedding
# ).from_loaders([loader])

# query = "请用markdown表格的方式列出所有具有防晒功能的衬衫，对每件衬衫描述进行总结"
# # 使用索引查询创建一个响应，并传入这个查询
# response = index.query(query)
# # 查看查询返回的内容
# display(Markdown(response))


from langchain_community.document_loaders import CSVLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings
import ollama

file = "./data/OutdoorClothingCatalog_1000.csv"
loader = CSVLoader(file_path=file)
documents = loader.load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=50)
chunks = text_splitter.split_documents(documents)
embedding = OllamaEmbeddings(model="nomic-embed-text")
vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embedding,
    persist_directory="./chroma_db",  # 向量数据库持久化目录
)
