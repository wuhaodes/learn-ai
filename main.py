import openai
import utils_zh
from tool import get_completion_from_messages

"""
注意：限于模型对中文理解能力较弱，中文 Prompt 可能会随机出现不成功，可以多次运行；也非常欢迎同学
探究更稳定的中文 Prompt
"""


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

    category_and_product_response = utils_zh.find_category_and_product_only(
        user_input, utils_zh.get_products_and_category()
    )
    # print(category_and_product_response)
    category_and_product_list = utils_zh.read_string_to_list(
        category_and_product_response
    )
    # print(category_and_product_list)
    if debug:
        print("第二步：抽取出商品列表")
    product_information = utils_zh.generate_output_string(category_and_product_list)
    if debug:
        print("第三步：查找抽取出的商品信息")

    # 第四步：根据信息生成回答
    system_message = f"""
    您是一家大型电子商店的客户服务助理。\
    请以友好和乐于助人的语气回答问题，并提供简洁明了的答案。\
    请确保向用户提出相关的后续问题。
    """
    # 插入 message
    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": f"{delimiter}{user_input}{delimiter}"},
        {"role": "assistant", "content": f"相关商品信息:\n{product_information}"},
    ]
    # 获取 GPT3.5 的回答
    # 通过附加 all_messages 实现多轮对话
    final_response = get_completion_from_messages(all_messages + messages)
    if debug:
        print("第四步：生成用户回答")
    # 将该轮信息加入到历史信息中
    all_messages = all_messages + messages[1:]
    # 第六步：模型检查是否很好地回答了用户问题
    user_message = f"""
    用户信息: {delimiter}{user_input}{delimiter}
    代理回复: {delimiter}{final_response}{delimiter}
    回复是否足够回答问题
    如果足够，回答 Y
    如果不足够，回答 N
    仅回答上述字母即可
    """
    # print(final_response)
    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": user_message},
    ]
    # 要求模型评估回答
    evaluation_response = get_completion_from_messages(messages)

    # print(evaluation_response)
    if debug:
        print("第六步：模型评估该回答")
    # 第七步：如果评估为 Y，输出回答；如果评估为 N，反馈将由人工修正答案
    if "Y" in evaluation_response:  # 使用 in 来避免模型可能生成 Yes
        if debug:
            print("第七步：模型赞同了该回答.")
        return final_response, all_messages
    else:
        if debug:
            print("第七步：模型不赞成该回答.")
        neg_str = "很抱歉，我无法提供您所需的信息。我将为您转接到一位人工客服代表以获取进一步帮助。"
    return neg_str, all_messages


user_input = "请告诉我关于 smartx pro phone 和 the fotosnap camera 的信息。另外，请告诉我关于你们的tvs的情况。"
response, _ = process_user_message_ch(user_input, [])
print(response)
