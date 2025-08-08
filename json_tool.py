import json

def get_json_str(filename):
    # 读取产品信息
    with open(filename, "r") as file:
        json_dict = json.load(file)
    return json_dict


def read_string_to_list(input_string):
    """
    将输入的字符串转换为 Python 列表。
    参数:
    input_string: 输入的字符串，应为有效的 JSON 格式。
    返回:
    list 或 None: 如果输入字符串有效，则返回对应的 Python 列表，否则返回 None。
    """
    if input_string is None:
        return None
    try:
        # 将输入字符串中的单引号替换为双引号，以满足 JSON 格式的要求
        input_string = input_string.replace("'", '"')
        data = json.loads(input_string)
        return data
    except json.JSONDecodeError:
        print("Error: Invalid JSON string")
        return None
