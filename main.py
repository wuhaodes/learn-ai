# from langchain_community.document_loaders import PyPDFLoader  # type: ignore
# from langchain_community.document_loaders.generic import GenericLoader  # type: ignore
# from langchain_community.document_loaders.parsers.audio import OpenAIWhisperParser  # type: ignore
# from langchain_community.document_loaders.blob_loaders.youtube_audio import YoutubeAudioLoader  # type: ignore

# url = "http://vd3.bdstatic.com/mda-ri168b4d5um4kbtf/360p/h264/1756787078853191638/mda-ri168b4d5um4kbtf.mp4"
# save_dir = "docs/video/"

# # 创建一个 GenericLoader Class 实例
# loader = GenericLoader(
#     # 将链接url中的Youtube视频的音频下载下来,存在本地路径save_dir
#     YoutubeAudioLoader([url], save_dir),
#     # 使用OpenAIWhisperPaser解析器将音频转化为文本
#     OpenAIWhisperParser(),
# )
# # 调用 GenericLoader Class 的函数 load对视频的音频文件进行加载
# pages = loader.load()

# print("Type of pages: ", type(pages))
# print("Length of pages: ", len(pages))
# page = pages[0]
# print("Type of page: ", type(page))
# print("Page_content: ", page.page_content[:500])
# print("Meta Data: ", page.metadata)

from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders.generic import GenericLoader
from langchain_community.document_loaders.blob_loaders.youtube_audio import (
    YoutubeAudioLoader,
)
from faster_whisper import WhisperModel


# 自定义本地Whisper解析器（替换OpenAIWhisperParser）
class LocalWhisperParser:
    def __init__(self, model_size="tiny", language=None):
        """
        初始化本地Whisper解析器

        参数:
            model_size: 模型大小(tiny/base/small/medium/large)
            language: 语言代码(如"zh"表示中文,"en"表示英文), None为自动检测
        """
        self.model = WhisperModel(model_size, device="cpu", compute_type="int8")
        self.language = language

    def parse(self, audio_path):
        """解析音频文件并返回转录文本"""
        segments, info = self.model.transcribe(
            audio_path, beam_size=5, language=self.language
        )
        text = "".join([seg.text for seg in segments])
        return [{"text": text}]


# 视频URL和保存目录
url = "http://vd3.bdstatic.com/mda-ri168b4d5um4kbtf/360p/h264/1756787078853191638/mda-ri168b4d5um4kbtf.mp4"
save_dir = "docs/video/"

# 创建加载器（使用本地解析器替换OpenAIWhisperParser）
loader = GenericLoader(
    YoutubeAudioLoader([url], save_dir),  # 下载YouTube音频
    LocalWhisperParser(model_size="tiny", language="zh"),  # 本地音频解析器
)

# 加载并转录音频
pages = loader.load()

# 输出结果
print("Type of pages: ", type(pages))
print("Length of pages: ", len(pages))
if pages:
    page = pages[0]
    print("Type of page: ", type(page))
    print("Page_content: ", page.page_content[:500])
    print("Meta Data: ", page.metadata)
else:
    print("未成功转录音频内容")
