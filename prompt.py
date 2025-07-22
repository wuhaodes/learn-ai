from tool import get_completion

# text = f"""
# 您应该提供尽可能清晰、具体的指示，以表达您希望模型执行的任务。\
# 这将引导模型朝向所需的输出，并降低收到无关或不正确响应的可能性。\
# 不要将写清晰的提示词与写简短的提示词混淆。\
# 在许多情况下，更长的提示词可以为模型提供更多的清晰度和上下文信息，从而导致更详细和相关的输出。
# """
# # 需要总结的文本内容
# prompt = f"""
# 把用三个反引号括起来的文本总结成一句话。
# 1.2 寻求结构化的输出
# 有时候我们需要语言模型给我们一些结构化的输出，而不仅仅是连续的文本。
# 什么是结构化输出呢？就是按照某种格式组织的内容，例如JSON、HTML等。这种输出非常适合在代码
# 中进一步解析和处理。例如，您可以在 Python 中将其读入字典或列表中。
# 在以下示例中，我们要求 GPT 生成三本书的标题、作者和类别，并要求 GPT 以 JSON 的格式返回给我
# 们，为便于解析，我们指定了 Json 的键。
# ```{text}```
# """
# # 指令内容，使用 ``` 来分隔指令和待总结的内容
# response = get_completion(prompt)
# print(response)


# prompt = f"""
# 请生成包括书名、作者和类别的三本虚构的、非真实存在的中文书籍清单，\
# 并以 JSON 格式提供，其中包含以下键:book_id、title、author、genre。
# """
# response = get_completion(prompt)
# print(response)


# 满足条件的输入（text中提供了步骤）
# text_1 = f"""
# 泡一杯茶很容易。首先，需要把水烧开。\
# 在等待期间，拿一个杯子并把茶包放进去。\
# 一旦水足够热，就把它倒在茶包上。\
# 等待一会儿，让茶叶浸泡。几分钟后，取出茶包。\
# 如果您愿意，可以加一些糖或牛奶调味。\
# 就这样，您可以享受一杯美味的茶了。
# """
# prompt = f"""
# 您将获得由三个引号括起来的文本。\
# 如果它包含一系列的指令，则需要按照以下格式重新编写这些指令：
# 第一步 - ...
# 第二步 - …
# …
# 第N步 - …
# 如果文本中不包含一系列的指令，则直接写“未提供步骤”。"
# \"\"\"{text_1}\"\"\"
# """
# response = get_completion(prompt)
# print("Text 1 的总结:")
# print(response)

# 不满足条件的输入（text中未提供预期指令）
# text_2 = f"""
# 今天阳光明媚，鸟儿在歌唱。\
# 这是一个去公园散步的美好日子。\
# 鲜花盛开，树枝在微风中轻轻摇曳。\
# 人们外出享受着这美好的天气，有些人在野餐，有些人在玩游戏或者在草地上放松。\
# 这是一个完美的日子，可以在户外度过并欣赏大自然的美景。
# 1.4 提供少量示例
# "Few-shot" prompting，即在要求模型执行实际任务之前，给模型一两个已完成的样例，让模型了解我
# 们的要求和期望的输出样式。
# 例如，在以下的样例中，我们先给了一个祖孙对话样例，然后要求模型用同样的隐喻风格回答关于“韧性”
# 的问题。这就是一个少样本样例，它能帮助模型快速抓住我们要的语调和风格。
# 利用少样本样例，我们可以轻松“预热”语言模型，让它为新的任务做好准备。这是一个让模型快速上手新
# 任务的有效策略。
# """
# prompt = f"""
# 您将获得由三个引号括起来的文本。\
# 如果它包含一系列的指令，则需要按照以下格式重新编写这些指令：
# 第一步 - ...
# 第二步 - …
# …
# 第N步 - …
# 如果文本中不包含一系列的指令，则直接写“未提供步骤”。"
# \"\"\"{text_2}\"\"\"
# """
# response = get_completion(prompt)
# print("Text 2 的总结:")
# print(response)

# prompt = f"""
# 您的任务是以一致的风格回答问题。
# 孩子: 请教我何为耐心。
# 祖父母: 挖出最深峡谷的河流源于一处不起眼的泉眼；最宏伟的交响乐从单一的音符开始；最复杂的挂毯以
# 一根孤独的线开始编织。
# 孩子: 请教我何为韧性。
# """
# response = get_completion(prompt)
# print(response)

# text = f"""
# 在一个迷人的村庄里，兄妹杰克和吉尔出发去一个山顶井里打水。\
# 他们一边唱着欢乐的歌，一边往上爬，\
# 然而不幸降临——杰克绊了一块石头，从山上滚了下来，吉尔紧随其后。\
# 虽然略有些摔伤，但他们还是回到了温馨的家中。\
# 尽管出了这样的意外，他们的冒险精神依然没有减弱，继续充满愉悦地探索。
# """
# # example 1
# prompt_1 = f"""
# 执行以下操作：
# 1-用一句话概括下面用三个反引号括起来的文本。
# 2-将摘要翻译成英语。
# 3-在英语摘要中列出每个人名。
# 4-输出一个 JSON 对象，其中包含以下键：english_summary，num_names。
# 请用换行符分隔您的答案。
# Text:
# ```{text}```
# """
# response = get_completion(prompt_1)
# print("prompt 1:")
# print(response)

# prompt_2 = f"""
# 1-用一句话概括下面用<>括起来的文本。
# 2-将摘要翻译成英语。
# 3-在英语摘要中列出每个名称。
# 4-输出一个 JSON 对象，其中包含以下键：English_summary，num_names。
# 请使用以下格式：
# 文本：<要总结的文本>
# 摘要：<摘要>
# 翻译：<摘要的翻译>
# 名称：<英语摘要中的名称列表>
# 输出 JSON：<带有 English_summary 和 num_names 的 JSON>
# Text: <{text}>
# """
# response = get_completion(prompt_2)
# print("\nprompt 2:")
# print(response)

# prompt = f"""
# 判断学生的解决方案是否正确。
# 问题:
# 我正在建造一个太阳能发电站，需要帮助计算财务。
# 土地费用为 100美元/平方英尺
# 我可以以 250美元/平方英尺的价格购买太阳能电池板
# 我已经谈判好了维护合同，每年需要支付固定的10万美元，并额外支付每平方英尺10美元
# 作为平方英尺数的函数，首年运营的总费用是多少。
# 学生的解决方案：
# 设x为发电站的大小，单位为平方英尺。
# 费用：
# 土地费用：100x
# 太阳能电池板费用：250x
# 维护费用：100,000美元+100x
# 总费用：100x+250x+100,000美元+100x=450x+100,000美元
# """
# response = get_completion(prompt)
# print(response)

# prompt = f"""
# 告诉我华为公司生产的GT Watch运动手表的相关信息
# """
# response = get_completion(prompt)
# print(response)

# 学习LLM-v1.0.0 学习到 四、1.1

# text = f"""
# You should express what you want a model to do by \
# providing instructions that are as clear and \
# specific as you can possibly make them. \
# This will guide the model towards the desired output, \
# and reduce the chances of receiving irrelevant \
# or incorrect responses. Don't confuse writing a \
# clear prompt with writing a short prompt. \
# In many cases, longer prompts provide more clarity \
# and context for the model, which can lead to \
# more detailed and relevant outputs.
# """
# prompt = f"""
# Summarize the text delimited by triple backticks \
# into a single sentence.
# ```{text}```
# """
# response = get_completion(prompt)
# print(response)

# prompt = f"""
# 列举一些心理学相关的书籍的名称 \
# 包含名称和出版社.请使用JSON格式且包含书籍唯一ID,名称,作者和出版社
# """
# response = get_completion(prompt)
# print(response)


# text_1 = f"""
# Making a cup of tea is easy! First, you need to get some \
# water boiling. While that's happening, \
# grab a cup and put a tea bag in it. Once the water is \
# hot enough, just pour it over the tea bag. \
# Let it sit for a bit so the tea can steep. After a \
# few minutes, take out the tea bag. If you \
# like, you can add some sugar or milk to taste. \
# And that's it! You've got yourself a delicious \
# cup of tea to enjoy.
# """
# prompt = f"""
# You will be provided with text delimited by triple quotes.
# If it contains a sequence of instructions, \
# re-write those instructions in the following format:
# 第1步 - ...
# 第2步 - …
# …
# 第N步 - …
# If the text does not contain a sequence of instructions, \
# then simply write \"No steps provided.\" 请以中文回答
# \"\"\"{text_1}\"\"\"
# """
# response = get_completion(prompt)
# print("煮茶的完整步骤:")
# print(response)

# text_2 = f"""
# The sun is shining brightly today, and the birds are \
# singing. It's a beautiful day to go for a \
# walk in the park. The flowers are blooming, and the \
# trees are swaying gently in the breeze. People \
# are out and about, enjoying the lovely weather. \
# Some are having picnics, while others are playing \
# games or simply relaxing on the grass. It's a \
# perfect day to spend time outdoors and appreciate the \
# beauty of nature.
# """
# prompt = f"""You will be provided with text delimited by triple quotes.
# If it contains a sequence of instructions, \
# re-write those instructions in the following format:
# Step 1 - ...
# Step 2 - …
# …
# Step N - …
# If the text does not contain a sequence of instructions, \
# then simply write \"No steps provided.\"
# \"\"\"{text_2}\"\"\"
# """
# response = get_completion(prompt)
# print("Completion for Text 2:")
# print(response)

# prompt = f"""
# 你的任务是以一致的风格回答。
# 外孙：教我耐心。
# 外公：雕刻最深的河流\
# 山谷从一个不起眼的泉水流出；the\
# 最伟大的交响乐源于一个音符； \
# 最复杂的挂毯始于一根单独的线。
# 外孙：教我韧性
# """
# response = get_completion(prompt)
# print(response)

# text = f"""
# 在一个迷人的村庄里，兄弟姐妹杰克和吉尔出发了\
# 从山顶取水的任务\
# 好。当他们攀登时，欢快地歌唱着，不幸\
# 杰克被石头绊倒了\
# 下了山，吉尔也跟着下了山。 \
# 虽然有点受伤，但两人还是回到了家\
# 安慰的拥抱。尽管发生了意外\
# 他们的冒险精神没有减弱，他们\
# 继续愉快地探索。
# """
# example 1
# prompt_1 = f"""
# 1-将摘要翻译成日语。
# 2-总结以下以三元组分隔的文本\
# 用1句话总结。
# 3-在日语摘要中列出每个名字。
# 4-输出一个包含以下内容的json对象\
# 关键字：french_summary，num_names。
# 文本：
# ```{text}```
# """
# response = get_completion(prompt_1)
# print("Completion for prompt 1:")
# print(response)

# prompt_2 = f"""
# Your task is to perform the following actions:
# 1 - Summarize the following text delimited by <> with 1 sentence.
# 2 - Translate the summary into Korean.
# 3 - List each name in the Korean summary.
# 4 - Output a json object that contains the
# following keys: korean_summary, num_names.
# Use the following format:
# Text: <text to summarize>
# Summary: <summary>
# Translation: <summary translation>
# Names: <list of names in Korean summary>
# Output JSON: <json with summary and num_names>
# Text: <{text}>
# """
# response = get_completion(prompt_2)
# print("\nCompletion for prompt 2:")
# print(response)

# prompt = f"""
# Determine if the student's solution is correct or not.
# Question:
# I'm building a solar power installation and I need \
# help working out the financials.
# - Land costs $100 / square foot
# - I can buy solar panels for $250 / square foot
# - I negotiated a contract for maintenance that will cost \
# me a flat $100k per year, and an additional $10 / square \
# foot
# What is the total cost for the first year of operations
# as a function of the number of square feet.
# Student's Solution:
# Let x be the size of the installation in square feet.
# Costs:
# 1. Land cost: 100x
# 2. Solar panel cost: 250x
# 3. Maintenance cost: 100,000 + 100x
# Total cost: 100x + 250x + 100,000 + 100x = 450x + 100,000
# """
# response = get_completion(prompt)
# print(response)

# prompt = f"""
# Your task is to determine if the student's solution \
# is correct or not.
# To solve the problem do the following:
# - First, work out your own solution to the problem.
# - Then compare your solution to the student's solution \
# and evaluate if the student's solution is correct or not.
# Don't decide if the student's solution is correct until
# you have done the problem yourself.
# Use the following format:
# Question:
# question here
# ```
# Student's solution:
# ```
# student's solution here
# ```
# Actual solution:
# ```
# steps to work out the solution and your solution here
# ```
# Is the student's solution the same as actual solution \
# just calculated:
# ```
# yes or no
# ```
# Student grade:
# ```
# correct or incorrect
# ```
# Question:
# ```
# I'm building a solar power installation and I need help \
# working out the financials.
# - Land costs $100 / square foot
# - I can buy solar panels for $250 / square foot
# - I negotiated a contract for maintenance that will cost \
# me a flat $100k per year, and an additional $10 / square \
# foot
# What is the total cost for the first year of operations \
# as a function of the number of square feet.
# ```
# Student's solution:
# ```
# Let x be the size of the installation in square feet.
# Costs:
# 1. Land cost: 100x
# 2. Solar panel cost: 250x
# 3. Maintenance cost: 100,000 + 100x
# Total cost: 100x + 250x + 100,000 + 100x = 450x + 100,000
# Actual solution:
# """
# response = get_completion(prompt)
# print(response)

# prompt = f"""
# Tell me about AeroGlide UltraSlim Smart Toothbrush by Boie
# """
# response = get_completion(prompt)
# print(response)
# prompt = f"""
# 告诉我Boie的AeroGlide超薄智能牙刷
# """
# response = get_completion(prompt)
# print(response)

# prompt = f"""
# 帮我查询深圳南山区这周的天气
# """
# response = get_completion(prompt)
# print(response)

# prompt = f"""
# 帮我分析一下利欧股份的股票行情，并给出一个短期操作的合理建议
# """
# response = get_completion(prompt)
# print(response)

# 学习到 <<第三章 迭代优化>>
fact_sheet_chair = """
概述
    美丽的中世纪风格办公家具系列的一部分，包括文件柜、办公桌、书柜、会议桌等。
    多种外壳颜色和底座涂层可选。
    可选塑料前后靠背装饰（SWC-100）或10种面料和6种皮革的全面装饰（SWC-110）。
    底座涂层选项为：不锈钢、哑光黑色、光泽白色或铬。
    椅子可带或不带扶手。
    适用于家庭或商业场所。
    符合合同使用资格。
结构
    五个轮子的塑料涂层铝底座。
    气动椅子调节，方便升降。
尺寸
    宽度53厘米|20.87英寸
    深度51厘米|20.08英寸
    高度80厘米|31.50英寸
    座椅高度44厘米|17.32英寸
    座椅深度41厘米|16.14英寸
选项
    软地板或硬地板滚轮选项。
    两种座椅泡沫密度可选：中等（1.8磅/立方英尺）或高（2.8磅/立方英尺）。
    无扶手或8个位置PU扶手。
材料
    外壳底座滑动件
    改性尼龙PA6/PA66涂层的铸铝。
    外壳厚度：10毫米。
    座椅
    HD36泡沫
原产国
    意大利
"""

# # Prompt ：基于说明书创建营销描述
# prompt = f"""
# 您的任务是帮助营销团队基于技术说明书创建一个产品的营销描述。
# 根据```标记的技术说明书中提供的信息，编写一个产品描述。
# 技术说明: ```{fact_sheet_chair}```
# """
# response = get_completion(prompt)
# print(response)

# 优化后的 Prompt，要求生成描述不多于 50 词
# prompt = f"""
# 您的任务是帮助营销团队基于技术说明书创建一个产品的零售网站描述。
# 根据```标记的技术说明书中提供的信息，编写一个产品描述。
# 使用最多50个词。
# 技术规格：```{fact_sheet_chair}```
# """
# response = get_completion(prompt)

# 优化后的 Prompt，说明面向对象，应具有什么性质且侧重于什么方面
# prompt = f"""
# 您的任务是帮助营销团队基于技术说明书创建一个产品的零售网站描述。
# 根据```标记的技术说明书中提供的信息，编写一个产品描述。
# 该描述面向家具零售商，因此应具有技术性质，并侧重于产品的材料构造。
# 使用最多50个汉字。
# 技术规格： ```{fact_sheet_chair}```
# """
# response = get_completion(prompt)

# 更进一步
# prompt = f"""
# 您的任务是帮助营销团队基于技术说明书创建一个产品的零售网站描述。
# 根据```标记的技术说明书中提供的信息，编写一个产品描述。
# 该描述面向家具零售商，因此应具有技术性质，并侧重于产品的材料构造。
# 在描述末尾，包括技术规格中每个7个字符的产品ID。
# 使用最多50个汉字。
# 技术规格： ```{fact_sheet_chair}```
# """

# from IPython.display import HTML, display
# import os
# import webbrowser
# # 要求它抽取信息并组织成表格，并指定表格的列、表名和格式
# prompt = f"""
# 您的任务是帮助营销团队基于技术说明书创建一个产品的零售网站描述。
# 根据```标记的技术说明书中提供的信息，编写一个产品描述。
# 该描述面向家具零售商，因此应具有技术性质，并侧重于产品的材料构造。
# 在描述末尾，包括技术规格中每个7个字符的产品ID。
# 在描述之后，包括一个表格，提供产品的尺寸。表格应该有两列。第一列包括尺寸的名称。第二列只包括英寸的
# 测量值。
# 给表格命名为“产品尺寸”。
# 将所有内容格式化为可用于网站的HTML格式。将描述放在<div>元素中。优化html样式。
# 除表格外最多使用50个汉字。
# 技术规格：```{fact_sheet_chair}```
# """
# response = get_completion(prompt)
# display(HTML(response))
# print(response)
# <IPython.core.display.HTML object>
# response = """```html
# <div style="font-family: Arial, sans-serif; line-height: 1.6; color: #333; max-width: 800px; margin: 0 auto;">
#     <p>中世纪风格办公椅，采用改性尼龙PA6/PA66涂层铸铝底座，五轮设计，气动升降。可选多种外壳颜色、底座涂层及装饰面料。座椅采用HD36泡沫，密度可选。意大利制造。</p>
    
#     <h3 style="margin-top: 20px;">产品尺寸</h3>
#     <table style="width: 100%; border-collapse: collapse; margin-top: 10px;">
#         <tr>
#             <th style="border: 1px solid #ddd; padding: 8px; text-align: left; background-color: #f2f2f2;">尺寸名称</th>
#             <th style="border: 1px solid #ddd; padding: 8px; text-align: left; background-color: #f2f2f2;">英寸</th>
#         </tr>
#         <tr>
#             <td style="border: 1px solid #ddd; padding: 8px;">宽度</td>
#             <td style="border: 1px solid #ddd; padding: 8px;">20.87</td>
#         </tr>
#         <tr>
#             <td style="border: 1px solid #ddd; padding: 8px;">深度</td>
#             <td style="border: 1px solid #ddd; padding: 8px;">20.08</td>
#         </tr>
#         <tr>
#             <td style="border: 1px solid #ddd; padding: 8px;">高度</td>
#             <td style="border: 1px solid #ddd; padding: 8px;">31.50</td>
#         </tr>
#         <tr>
#             <td style="border: 1px solid #ddd; padding: 8px;">座椅高度</td>
#             <td style="border: 1px solid #ddd; padding: 8px;">17.32</td>
#         </tr>
#         <tr>
#             <td style="border: 1px solid #ddd; padding: 8px;">座椅深度</td>
#             <td style="border: 1px solid #ddd; padding: 8px;">16.14</td>
#         </tr>
#     </table>
    
#     <p style="margin-top: 20px;">产品ID: SWC-100 / SWC-110</p>
# </div>
# ```
# """
# html_str = response.replace("```html", "").replace("```", "")
# html = f"""
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>办公座椅产品描述</title>
# </head>
# <body>
# {html_str}
# </body>
# </html>
# """
# with open("temp.html", "w") as file:
#     file.write(html)

# # # 使用默认的网页浏览器打开文件
# webbrowser.open("file://" + os.path.realpath("temp.html"))

# 学习到 <<二、总结>>