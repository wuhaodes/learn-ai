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
# fact_sheet_chair = """
# 概述
#     美丽的中世纪风格办公家具系列的一部分，包括文件柜、办公桌、书柜、会议桌等。
#     多种外壳颜色和底座涂层可选。
#     可选塑料前后靠背装饰（SWC-100）或10种面料和6种皮革的全面装饰（SWC-110）。
#     底座涂层选项为：不锈钢、哑光黑色、光泽白色或铬。
#     椅子可带或不带扶手。
#     适用于家庭或商业场所。
#     符合合同使用资格。
# 结构
#     五个轮子的塑料涂层铝底座。
#     气动椅子调节，方便升降。
# 尺寸
#     宽度53厘米|20.87英寸
#     深度51厘米|20.08英寸
#     高度80厘米|31.50英寸
#     座椅高度44厘米|17.32英寸
#     座椅深度41厘米|16.14英寸
# 选项
#     软地板或硬地板滚轮选项。
#     两种座椅泡沫密度可选：中等（1.8磅/立方英尺）或高（2.8磅/立方英尺）。
#     无扶手或8个位置PU扶手。
# 材料
#     外壳底座滑动件
#     改性尼龙PA6/PA66涂层的铸铝。
#     外壳厚度：10毫米。
#     座椅
#     HD36泡沫
# 原产国
#     意大利
# """

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

# fact_sheet_chair = """
# OVERVIEW
# - Part of a beautiful family of mid-century inspired office furniture,
# including filing cabinets, desks, bookcases, meeting tables, and more.
# - Several options of shell color and base finishes.
# - Available with plastic back and front upholstery (SWC-100)
# or full upholstery (SWC-110) in 10 fabric and 6 leather options.
# - Base finish options are: stainless steel, matte black,
# gloss white, or chrome.
# - Chair is available with or without armrests.
# - Suitable for home or business settings.
# - Qualified for contract use.
# CONSTRUCTION
# - 5-wheel plastic coated aluminum base.
# - Pneumatic chair adjust for easy raise/lower action.
# DIMENSIONS
# - WIDTH 53 CM | 20.87”
# - DEPTH 51 CM | 20.08”
# - HEIGHT 80 CM | 31.50”
# - SEAT HEIGHT 44 CM | 17.32”
# - SEAT DEPTH 41 CM | 16.14”
# OPTIONS
# - Soft or hard-floor caster options.
# - Two choices of seat foam densities:
# medium (1.8 lb/ft3) or high (2.8 lb/ft3)
# - Armless or 8 position PU armrests
# MATERIALS
# SHELL BASE GLIDER
# - Cast Aluminum with modified nylon PA6/PA66 coating.
# - Shell thickness: 10 mm.
# SEAT
# - HD36 foam
# COUNTRY OF ORIGIN
# - Italy
# """
# Prompt ：基于说明书生成营销描述
# prompt = f"""
# Your task is to help a marketing team create a
# description for a retail website of a product based
# on a technical fact sheet.
# Write a product description based on the information
# provided in the technical specifications delimited by
# triple backticks.
# Technical specifications: ```{fact_sheet_chair}```
# """
# response = get_completion(prompt)
# print(response)

# 优化后的 Prompt，要求生成描述不多于 50 词
# prompt = f"""
# Your task is to help a marketing team create a
# description for a retail website of a product based
# on a technical fact sheet.
# Write a product description based on the information
# provided in the technical specifications delimited by
# triple backticks.
# Use at most 50 words.
# Technical specifications: ```{fact_sheet_chair}```
# """
# response = get_completion(prompt)
# print(response)

# 优化后的 Prompt，说明面向对象，应具有什么性质且侧重于什么方面
# prompt = f"""
# Your task is to help a marketing team create a
# description for a retail website of a product based
# on a technical fact sheet.
# Write a product description based on the information
# provided in the technical specifications delimited by
# triple backticks.
# The description is intended for furniture retailers,
# so should be technical in nature and focus on the
# materials the product is constructed from.
# Use at most 50 words.
# Technical specifications: ```{fact_sheet_chair}```
# """
# response = get_completion(prompt)
# print(response)

# 更进一步，要求在描述末尾包含 7个字符的产品ID
# prompt = f"""
# Your task is to help a marketing team create a
# description for a retail website of a product based
# on a technical fact sheet.
# Write a product description based on the information
# provided in the technical specifications delimited by
# triple backticks.
# The description is intended for furniture retailers,
# so should be technical in nature and focus on the
# materials the product is constructed from.
# At the end of the description, include every 7-character
# Product ID in the technical specification.
# Use at most 50 words.
# Technical specifications: ```{fact_sheet_chair}```
# """
# response = get_completion(prompt)
# print(response)

# 要求它抽取信息并组织成表格，并指定表格的列、表名和格式
# prompt = f"""
# Your task is to help a marketing team create a
# description for a retail website of a product based
# on a technical fact sheet.
# Write a product description based on the information
# provided in the technical specifications delimited by
# triple backticks.
# The description is intended for furniture retailers,
# so should be technical in nature and focus on the
# materials the product is constructed from.
# At the end of the description, include every 7-character
# Product ID in the technical specification.
# After the description, include a table that gives the
# product's dimensions. The table should have two columns.
# In the first column include the name of the dimension.
# In the second column include the measurements in inches only.
# Give the table the title 'Product Dimensions'.
# Format everything as HTML that can be used in a website.
# Place the description in a <div> element.
# Technical specifications: ```{fact_sheet_chair}```
# """
# response = get_completion(prompt)
# print(response)
# # 表格是以 HTML 格式呈现的，加载出来
# from IPython.display import display, HTML
# display(HTML(response))

# 学习到 <<第四章 文本概括>>

# prod_review = """
# 这个熊猫公仔是我给女儿的生日礼物，她很喜欢，去哪都带着。
# 公仔很软，超级可爱，面部表情也很和善。但是相比于价钱来说，
# 它有点小，我感觉在别的地方用同样的价钱能买到更大的。
# 快递比预期提前了一天到货，所以在送给女儿之前，我自己玩了会。
# """

# prompt = f"""
# 您的任务是从电子商务网站上生成一个产品评论的简短摘要。
# 请对三个反引号之间的评论文本进行概括，最多30个字。
# 评论: ```{prod_review}```
# """
# response = get_completion(prompt)
# print(response)

# prompt = f"""
# 您的任务是从电子商务网站上生成一个产品评论的简短摘要。
# 请对三个反引号之间的评论文本进行概括，最多30个字，并且侧重在快递服务上。
# 评论: ```{prod_review}```
# """
# response = get_completion(prompt)
# print(response)

# prompt = f"""
# 您的任务是从电子商务网站上生成一个产品评论的简短摘要。
# 请对三个反引号之间的评论文本进行概括，最多30个词汇，并且侧重在产品价格和质量上。
# 评论: ```{prod_review}```
# """
# response = get_completion(prompt)
# print(response)

# prompt = f"""
# 您的任务是从电子商务网站上的产品评论中提取相关信息。
# 请从以下三个反引号之间的评论文本中提取产品运输相关的信息，最多30个词汇。
# 评论: ```{prod_review}```
# """
# response = get_completion(prompt)
# print(response)

# review_1 = prod_review
# # 一盏落地灯的评论
# review_2 = """
# 我需要一盏漂亮的卧室灯，这款灯不仅具备额外的储物功能，价格也并不算太高。
# 收货速度非常快，仅用了两天的时间就送到了。
# 不过，在运输过程中，灯的拉线出了问题，幸好，公司很乐意寄送了一根全新的灯线。
# 新的灯线也很快就送到手了，只用了几天的时间。
# 装配非常容易。然而，之后我发现有一个零件丢失了，于是我联系了客服，他们迅速地给我寄来了缺失的零件！
# 对我来说，这是一家非常关心客户和产品的优秀公司。
# """
# # 一把电动牙刷的评论
# review_3 = """
# 我的牙科卫生员推荐了电动牙刷，所以我就买了这款。
# 到目前为止，电池续航表现相当不错。
# 初次充电后，我在第一周一直将充电器插着，为的是对电池进行条件养护。
# 过去的3周里，我每天早晚都使用它刷牙，但电池依然维持着原来的充电状态。
# 不过，牙刷头太小了。我见过比这个牙刷头还大的婴儿牙刷。
# 我希望牙刷头更大一些，带有不同长度的刷毛，
# 这样可以更好地清洁牙齿间的空隙，但这款牙刷做不到。
# 总的来说，如果你能以50美元左右的价格购买到这款牙刷，那是一个不错的交易。
# 制造商的替换刷头相当昂贵，但你可以购买价格更为合理的通用刷头。
# 这款牙刷让我感觉就像每天都去了一次牙医，我的牙齿感觉非常干净！
# """
# # 一台搅拌机的评论
# review_4 = """
# 在11月份期间，这个17件套装还在季节性促销中，售价约为49美元，打了五折左右。
# 可是由于某种原因（我们可以称之为价格上涨），到了12月的第二周，所有的价格都上涨了，
# 同样的套装价格涨到了70-89美元不等。而11件套装的价格也从之前的29美元上涨了约10美元。
# 看起来还算不错，但是如果你仔细看底座，刀片锁定的部分看起来没有前几年版本的那么漂亮。
# 然而，我打算非常小心地使用它
# （例如，我会先在搅拌机中研磨豆类、冰块、大米等坚硬的食物，然后再将它们研磨成所需的粒度，
# 接着切换到打蛋器刀片以获得更细的面粉，如果我需要制作更细腻/少果肉的食物）。
# 在制作冰沙时，我会将要使用的水果和蔬菜切成细小块并冷冻
# （如果使用菠菜，我会先轻微煮熟菠菜，然后冷冻，直到使用时准备食用。
# 如果要制作冰糕，我会使用一个小到中号的食物加工器），这样你就可以避免添加过多的冰块。
# 大约一年后，电机开始发出奇怪的声音。我打电话给客户服务，但保修期已经过期了，
# 所以我只好购买了另一台。值得注意的是，这类产品的整体质量在过去几年里有所下降
# ，所以他们在一定程度上依靠品牌认知和消费者忠诚来维持销售。在大约两天内，我收到了新的搅拌机。
# """
# reviews = [review_1, review_2, review_3, review_4]

# for i in range(len(reviews)):
#     prompt = f"""
#     你的任务是从电子商务网站上的产品评论中提取相关信息。
#     请对三个反引号之间的评论文本进行概括，最多20个词汇。
#     评论文本: ```{reviews[i]}```
#     """
#     print(f"评论{i+1}:\n", get_completion(prompt), "\n")

# prod_review = """
# Got this panda plush toy for my daughter's birthday, \
# who loves it and takes it everywhere. It's soft and \
# super cute, and its face has a friendly look. It's \
# a bit small for what I paid though. I think there \
# might be other options that are bigger for the \
# same price. It arrived a day earlier than expected, \
# so I got to play with it myself before I gave it \
# to her.
# """
# prompt = f"""
# Your task is to generate a short summary of a product \
# review from an ecommerce site.
# Summarize the review below, delimited by triple
# backticks, in at most 30 words.
# Review: ```{prod_review}```
# """
# response = get_completion(prompt)
# print(response)

# prompt = f"""
# Your task is to generate a short summary of a product \
# review from an ecommerce site to give feedback to the \
# Shipping deparmtment.
# Summarize the review below, delimited by triple
# backticks, in at most 30 words, and focusing on any aspects \
# that mention shipping and delivery of the product.
# Review: ```{prod_review}```
# """
# response = get_completion(prompt)
# print(response)

# prompt = f"""
# Your task is to generate a short summary of a product \
# review from an ecommerce site to give feedback to the \
# pricing deparmtment, responsible for determining the \
# price of the product.
# Summarize the review below, delimited by triple
# backticks, in at most 30 words, and focusing on any aspects \
# that are relevant to the price and perceived value.
# Review: ```{prod_review}```
# """
# response = get_completion(prompt)
# print(response)

# prompt = f"""
# Your task is to extract relevant information from \
# a product review from an ecommerce site to give \
# feedback to the Shipping department.
# From the review below, delimited by triple quotes \
# extract the information relevant to shipping and \
# delivery. Limit to 30 words.
# Review: ```{prod_review}```
# """
# response = get_completion(prompt)
# print(response)

# review_1 = prod_review
# # review for a standing lamp
# review_2 = """
# Needed a nice lamp for my bedroom, and this one \
# had additional storage and not too high of a price \
# point. Got it fast - arrived in 2 days. The string \
# to the lamp broke during the transit and the company \
# happily sent over a new one. Came within a few days \
# as well. It was easy to put together. Then I had a \
# missing part, so I contacted their support and they \
# very quickly got me the missing piece! Seems to me \
# to be a great company that cares about their customers \
# and products.
# """
# # review for an electric toothbrush
# review_3 = """
# My dental hygienist recommended an electric toothbrush, \
# which is why I got this. The battery life seems to be \
# pretty impressive so far. After initial charging and \
# leaving the charger plugged in for the first week to \
# condition the battery, I've unplugged the charger and \
# been using it for twice daily brushing for the last \
# 3 weeks all on the same charge. But the toothbrush head \
# is too small. I’ve seen baby toothbrushes bigger than \
# this one. I wish the head was bigger with different \
# length bristles to get between teeth better because \
# this one doesn’t. Overall if you can get this one \
# around the $50 mark, it's a good deal. The manufactuer's \
# replacements heads are pretty expensive, but you can \
# get generic ones that're more reasonably priced. This \
# toothbrush makes me feel like I've been to the dentist \
# every day. My teeth feel sparkly clean!
# """
# # review for a blender
# review_4 = """
# So, they still had the 17 piece system on seasonal \
# sale for around $49 in the month of November, about \
# half off, but for some reason (call it price gouging) \
# around the second week of December the prices all went \
# up to about anywhere from between $70-$89 for the same \
# system. And the 11 piece system went up around $10 or \
# so in price also from the earlier sale price of $29. \
# So it looks okay, but if you look at the base, the part \
# where the blade locks into place doesn’t look as good \
# as in previous editions from a few years ago, but I \
# plan to be very gentle with it (example, I crush \
# very hard items like beans, ice, rice, etc. in the \
# blender first then pulverize them in the serving size \
# I want in the blender then switch to the whipping \
# blade for a finer flour, and use the cross cutting blade \
# first when making smoothies, then use the flat blade \
# if I need them finer/less pulpy). Special tip when making \
# smoothies, finely cut and freeze the fruits and \
# vegetables (if using spinach-lightly stew soften the \
# spinach then freeze until ready for use-and if making \
# sorbet, use a small to medium sized food processor) \
# that you plan to use that way you can avoid adding so \
# much ice if at all-when making your smoothie. \
# After about a year, the motor was making a funny noise. \
# I called customer service but the warranty expired \
# already, so I had to buy another one. FYI: The overall \
# quality has gone done in these types of products, so \
# they are kind of counting on brand recognition and \
# consumer loyalty to maintain sales. Got it in about \
# two days
# """

# reviews = [review_1, review_2, review_3, review_4]

# for i in range(len(reviews)):
#     prompt = f"""
#     Your task is to generate a short summary of a product \
#     review from an ecommerce site.
#     Summarize the review below, delimited by triple \
#     backticks in at most 20 words.
#     Review: ```{reviews[i]}```
#     """
#     response = get_completion(prompt)
#     print(i+1, response, "\n")

# lamp_review = """
# 我需要一盏漂亮的卧室灯，这款灯具有额外的储物功能，价格也不算太高。\
# 我很快就收到了它。在运输过程中，我们的灯绳断了，但是公司很乐意寄送了一个新的。\
# 几天后就收到了。这款灯很容易组装。我发现少了一个零件，于是联系了他们的客服，他们很快就给我寄来了缺
# 失的零件！\
# 在我看来，Lumina 是一家非常关心顾客和产品的优秀公司！
# """

# prompt = f"""
# 以下用三个反引号分隔的产品评论的情感是什么？
# 评论文本: ```{lamp_review}```
# """
# response = get_completion(prompt)
# print(response)

# prompt = f"""
# 以下用三个反引号分隔的产品评论的情感是什么？
# 用一个单词回答：「正面」或「负面」。
# 评论文本: ```{lamp_review}```
# """
# response = get_completion(prompt)
# print(response)

# 中文
# prompt = f"""
# 识别以下评论的作者表达的情感。包含不超过五个项目。将答案格式化为以逗号分隔的中文单词列表。
# 评论文本: ```{lamp_review}```
# """
# response = get_completion(prompt)
# print(response)

# # 中文
# prompt = f"""
# 以下评论的作者是否表达了愤怒？评论用三个反引号分隔。给出是或否的答案。
# 评论文本: ```{lamp_review}```
# """
# response = get_completion(prompt)
# print(response)

# # 中文
# prompt = f"""
# 从评论文本中识别以下项目：
# - 评论者购买的物品
# - 制造该物品的公司
# 评论文本用三个反引号分隔。将你的响应格式化为以 “物品” 和 “品牌” 为键的 JSON 对象。
# 如果信息不存在，请使用 “未知” 作为值。
# 让你的回应尽可能简短。
# 评论文本: ```{lamp_review}```
# """
# response = get_completion(prompt)
# print(response)

# # 中文
# prompt = f"""
# 从评论文本中识别以下项目：
# - 情绪（正面或负面）
# - 审稿人是否表达了愤怒？（是或否）
# - 评论者购买的物品
# - 制造该物品的公司
# 评论用三个反引号分隔。将你的响应格式化为 JSON 对象，以 “情感倾向”、“是否生气”、“物品类型” 和
# “品牌” 作为键。
# 如果信息不存在，请使用 “未知” 作为值。
# 让你的回应尽可能简短。
# 将 “是否生气” 值格式化为布尔值。
# 评论文本: ```{lamp_review}```
# """
# response = get_completion(prompt)
# print(response)

# 学习到 <<三、主题推断>>

# # 中文
# story = """
# 在政府最近进行的一项调查中，要求公共部门的员工对他们所在部门的满意度进行评分。
# 调查结果显示，NASA 是最受欢迎的部门，满意度为 95％。
# 一位 NASA 员工 John Smith 对这一发现发表了评论，他表示：
# “我对 NASA 排名第一并不感到惊讶。这是一个与了不起的人们和令人难以置信的机会共事的好地方。我为成
# 为这样一个创新组织的一员感到自豪。”
# NASA 的管理团队也对这一结果表示欢迎，主管 Tom Johnson 表示：
# “我们很高兴听到我们的员工对 NASA 的工作感到满意。
# 我们拥有一支才华横溢、忠诚敬业的团队，他们为实现我们的目标不懈努力，看到他们的辛勤工作得到回报是太
# 棒了。”
# 调查还显示，社会保障管理局的满意度最低，只有 45％的员工表示他们对工作满意。
# 政府承诺解决调查中员工提出的问题，并努力提高所有部门的工作满意度。
# """

# # 中文
# prompt = f"""
# 确定以下给定文本中讨论的五个主题。
# 每个主题用1-2个词概括。
# 请输出一个可解析的Python列表，每个元素是一个字符串，展示了一个主题。
# 给定文本: ```{story}```
# """
# response = get_completion(prompt)
# print(response)

# # 中文
# prompt = f"""
# 判断主题列表中的每一项是否是给定文本中的一个话题，
# 以列表的形式给出答案，每个元素是一个Json对象，键为对应主题，值为对应的 0 或 1。
# 主题列表：美国航空航天局、当地政府、工程、员工满意度、联邦政府
# 给定文本: ```{story}```
# """
# response = get_completion(prompt)
# print(response)
# result = response.replace("`", "").replace("json\n", "")
# result_lst = eval(result)
# topic_dict = {list(i.keys())[0]: list(i.values())[0] for i in result_lst}
# print(topic_dict)
# if topic_dict["美国航空航天局"] == 1:
#     print("提醒: 关于美国航空航天局的新消息")

# lamp_review = """
# Needed a nice lamp for my bedroom, and this one had \
# additional storage and not too high of a price point. \
# Got it fast. The string to our lamp broke during the \
# transit and the company happily sent over a new one. \
# Came within a few days as well. It was easy to put \
# together. I had a missing part, so I contacted their \
# support and they very quickly got me the missing piece! \
# Lumina seems to me to be a great company that cares \
# about their customers and products!!
# """
# prompt = f"""
# What is the sentiment of the following product review,
# which is delimited with triple backticks?
# Review text: ```{lamp_review}```
# """
# response = get_completion(prompt)
# print(response)

# prompt = f"""
# What is the sentiment of the following product review,
# which is delimited with triple backticks?
# Give your answer as a single word, either "positive" \
# or "negative".
# Review text: ```{lamp_review}```
# """
# response = get_completion(prompt)
# print(response)

# prompt = f"""
# Identify a list of emotions that the writer of the \
# following review is expressing. Include no more than \
# five items in the list. Format your answer as a list of \
# lower-case words separated by commas.
# Review text: ```{lamp_review}```
# """
# response = get_completion(prompt)
# print(response)

# prompt = f"""
# Is the writer of the following review expressing anger?\
# The review is delimited with triple backticks. \
# Give your answer as either yes or no.
# Review text: ```{lamp_review}```
# """
# response = get_completion(prompt)
# print(response)

# prompt = f"""
# Identify the following items from the review text:
# - Item purchased by reviewer
# - Company that made the item
# The review is delimited with triple backticks. \
# Format your response as a JSON object with \
# "Item" and "Brand" as the keys.
# If the information isn't present, use "unknown" \
# as the value.
# Make your response as short as possible.
# Review text: ```{lamp_review}```
# """
# response = get_completion(prompt)
# print(response)

# prompt = f"""
# Identify the following items from the review text:
# - Sentiment (positive or negative)
# - Is the reviewer expressing anger? (true or false)
# - Item purchased by reviewer
# - Company that made the item
# The review is delimited with triple backticks. \
# Format your response as a JSON object with \
# "Sentiment", "Anger", "Item" and "Brand" as the keys.
# If the information isn't present, use "unknown" \
# as the value.
# Make your response as short as possible.
# Format the Anger value as a boolean.
# Review text: ```{lamp_review}```
# """
# response = get_completion(prompt)
# print(response)

# 3.1 推断讨论主题

# story = """
# In a recent survey conducted by the government,
# public sector employees were asked to rate their level
# of satisfaction with the department they work at.
# The results revealed that NASA was the most popular
# department with a satisfaction rating of 95%.
# One NASA employee, John Smith, commented on the findings,
# stating, "I'm not surprised that NASA came out on top.
# It's a great place to work with amazing people and
# incredible opportunities. I'm proud to be a part of
# such an innovative organization."
# The results were also welcomed by NASA's management team,
# with Director Tom Johnson stating, "We are thrilled to
# hear that our employees are satisfied with their work at NASA.
# We have a talented and dedicated team who work tirelessly
# to achieve our goals, and it's fantastic to see that their
# hard work is paying off."
# The survey also revealed that the
# Social Security Administration had the lowest satisfaction
# rating, with only 45% of employees indicating they were
# satisfied with their job. The government has pledged to
# address the concerns raised by employees in the survey and
# work towards improving job satisfaction across all departments.
# """
# prompt = f"""
# Determine five topics that are being discussed in the \
# following text, which is delimited by triple backticks.
# Make each item one or two words long.
# Format your response as a list of items separated by commas.
# Give me a list which can be read in Python.
# Text sample: ```{story}```
# """
# response = get_completion(prompt)
# print(response)

# topic_list = [
#     "nasa",
#     "local government",
#     "engineering",
#     "employee satisfaction",
#     "federal government",
# ]
# prompt = f"""
# Determine whether each item in the following list of \
# topics is a topic in the text below, which
# is delimited with triple backticks.
# Give your answer as list with 0 or 1 for each topic.\
# List of topics: {", ".join(topic_list)}
# Text sample: ```{story}```
# """
# response = get_completion(prompt)
# print(response)

# 学习到 《3.2 为特定主题制作新闻提醒》

# topic_list = [
#     "nasa",
#     "local government",
#     "engineering",
#     "employee satisfaction",
#     "federal government",
# ]
# prompt = f"""
# Determine whether each item in the following list of \
# topics is a topic in the text below, which
# is delimited with triple backticks.
# Give your answer as list with 0 or 1 for each topic.\
# please only give a list for answer.\
# List of topics: {", ".join(topic_list)}
# Text sample: ```{story}```
# """
# response = get_completion(prompt)
# print(response)

# topic_dict = {topic_list[i]: eval(response)[i] for i in range(len(eval(response)))}
# print(topic_dict)
# if topic_dict["nasa"] == 1:
#     print("ALERT: New NASA story!")

# prompt = f"""
# 将以下中文翻译成甲骨文,按照下列格式给出翻译结果去掉解释过程及详解: \
# ```您好，我想订购一个搅拌机。```
# """
# response = get_completion(prompt)
# print(response)

# prompt = f"""
# 请告诉我以下文本是什么语种,并翻译为中文.
# 按照格式 <结果语种>==><中文>: 翻译结果\
# 格式不需要输出\
# 文本如下:
# ```Combien coûte le lampadaire?```
# """
# response = get_completion(prompt)
# print(response)

# prompt = f"""
# 请将以下文本分别翻译成中文、英文、法语和西班牙语.\
# 输出格式输出格式为: <语种>: <翻译结果>\
# 文本如下:\
# ```I want to order a basketball.```
# """
# response = get_completion(prompt)
# print(response)

# prompt = f"""
# 请将以下文本翻译成中文、英文、法语和西班牙语，分别展示成正式与非正式两种语气.
# 输出格式为: <语种-语气>: <翻译结果>\
# ```Would you like to order a pillow?```
# """
# response = get_completion(prompt)
# print(response)

# user_messages = [
# "La performance du système est plus lente que d'habitude.", # System performance is slower than normal
# "Mi monitor tiene píxeles que no se iluminan.", # My monitor has pixels that are not lighting
# "Il mio mouse non funziona", # My mouse is not working
# "Mój klawisz Ctrl jest zepsuty", # My keyboard has a broken control key
# "我的屏幕在闪烁" # My screen is flashing
# ]

# import time
# for message in user_messages:
#     time.sleep(20)
#     prompt = f"告诉我以下文本是什么语种，直接输出语种，如法语，无需输出标点符号:\
#     ```{message}```"
#     lang = get_completion(prompt)
#     print(f"原始消息 ({lang}): {message}\n")
#     prompt = f"""
#     将以下消息分别翻译成英文和中文，并写成
#     中文翻译：xxx
#     英文翻译：yyy
#     的格式：
#     ```{message}```
#     """
#     response = get_completion(prompt)
#     print(response, "\n=========================================")

# 学习到 <<二、语气与写作风格调整>>