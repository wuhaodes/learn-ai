# from tool1 import collect_messages # type: ignore
from tool import get_completion_and_token_count

# a = collect_messages()
# print(a)


# response = get_completion("中国的首都是哪里？")
# print(response)

# 为了更好展示效果，这里就没有翻译成中文的 Prompt
# 注意这里的字母翻转出现了错误，吴恩达老师正是通过这个例子来解释 token 的计算方式
# response = get_completion(
#     "Take the letters in lollipop \
# and reverse them"
# )
# print(response)

# response = get_completion(
#     """Take the letters in \
# l-o-l-l-i-p-o-p and reverse them"""
# )
# print(response)

# messages = [
#     {"role": "system", "content": "你是一个助理， 并以 Seuss 苏斯博士的风格作出回答。"},
#     {"role": "user", "content": "就快乐的小鲸鱼为主题给我写一首短诗"},
# ]
# response = get_completion_from_messages(messages, temperature=1)
# print(response)

# messages = [
#     {"role": "system", "content": "你的所有答复只能是一句话"},
#     {"role": "user", "content": "写一个关于快乐的小鲸鱼的故事"},
# ]
# response = get_completion_from_messages(messages, temperature=1)
# print(response)

# messages = [
#     {
#         "role": "system",
#         "content": "你是一个助理， 并以 Seuss 苏斯博士的风格作出回答，只回答一句话",
#     },
#     {"role": "user", "content": "写一个关于快乐的小鲸鱼的故事"},
# ]
# response = get_completion_from_messages(messages, temperature=1)
# print(response)


# messages = [
# {'role':'system',
# 'content':'你是一个助理， 并以 Seuss 苏斯博士的风格作出回答。'},
# {'role':'user',
# 'content':'就快乐的小鲸鱼为主题给我写一首短诗'},
# ]
# response, token_dict = get_completion_and_token_count(messages)
# print(response)
# print(token_dict)

# 学习到 第三章 评估输入——分类