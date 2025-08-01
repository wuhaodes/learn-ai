# from tool1 import collect_messages # type: ignore
from tool import get_completion

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
