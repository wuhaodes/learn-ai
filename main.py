# 第五章 基于文档的问答
from langchain_openai import ChatOpenAI  # type: ignore
from langchain_community.document_loaders import CSVLoader  # type: ignore
from langchain.text_splitter import RecursiveCharacterTextSplitter  # type: ignore
from langchain_community.vectorstores import Chroma  # type: ignore
from langchain_community.embeddings import OllamaEmbeddings  # type: ignore
from langchain.chains import RetrievalQA # type: ignore #检索QA链，在文档上进行检索
from tool import get_openai_key

api_key = get_openai_key()
llm = ChatOpenAI(
    model="deepseek-reasoner",
    api_key=api_key,
    base_url="https://api.deepseek.com",
    temperature=0.0,
)

file = "./data/OutdoorClothingCatalog_1000.csv"
loader = CSVLoader(file_path=file)
documents = loader.load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=50)
chunks = text_splitter.split_documents(documents)
embedding = OllamaEmbeddings(model="nomic-embed-text")
db = Chroma.from_documents(
    documents=chunks,
    embedding=embedding,
    persist_directory="./chroma_db",  # 向量数据库持久化目录
)

query = "请推荐一件具有防晒功能的衬衫"
# 在向量数据库中搜索相似内容
docs = db.similarity_search(query)  # k 表示返回最相似的前 k 个结果
# q_docs = "".join([docs[i].page_content for i in range(len(docs))])
# #将合并的相似文档内容后加上问题（question）输入到 `llm.call_as_llm`中
# #这里问题是：以Markdown表格的方式列出所有具有防晒功能的衬衫并总结
# response = llm.call_as_llm(f"{q_docs}问题：请用markdown表格的方式列出所有具有防晒功能的衬衫，对每件衬衫描述进行总结")
# print(response)

retriever = db.as_retriever()
qa_stuff = RetrievalQA.from_chain_type(
llm=llm,
chain_type="stuff",
retriever=retriever,
verbose=True
)
#创建一个查询并在此查询上运行链
query = "请用markdown表格的方式列出所有具有防晒功能的衬衫，对每件衬衫描述进行总结"
response = qa_stuff.run(query)
print(response)

# 第六章 评估