import openai # type: ignore
import utils_zh # type: ignore
from tool import get_completion_from_messages

'''
注意：限于模型对中文理解能力较弱，中文 Prompt 可能会随机出现不成功，可以多次运行；也非常欢迎同学
探究更稳定的中文 Prompt
'''

def process_user_message_ch(user_input, all_messages, debug=True):
    """
    对用户信息进行预处理
    参数:
    user_input : 用户输入
    all_messages : 历史信息
    debug : 是否开启 DEBUG 模式,默认开启
    """
    # 分隔符
    delimiter = "```"
    # 第一步: 使用 OpenAI 的 Moderation API 检查用户输入是否合规或者是一个注入的 Prompt