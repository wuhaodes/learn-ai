# 第九章 评估（上）——存在一个简单的正确答案
# import utils_zh
# import json
# import time
# from tool import get_completion_from_messages

# products_and_category = utils_zh.get_products_and_category()
# print(products_and_category)


# def find_category_and_product_v1(user_input, products_and_category):
#     """
#     从用户输入中获取到产品和类别
#     参数：
#     user_input：用户的查询
#     products_and_category：产品类型和对应产品的字典
#     """
#     delimiter = "####"
#     system_message = f"""
#     您将提供客户服务查询。\
#     客户服务查询将用{delimiter}字符分隔。
#     输出一个 Python 列表，列表中的每个对象都是 Json 对象，每个对象的格式如下：
#     '类别': <电脑和笔记本, 智能手机和配件, 电视和家庭影院系统, \
#     游戏机和配件, 音频设备, 相机和摄像机中的一个>,
#     以及
#     '名称': <必须在下面允许的产品中找到的产品列表>
#     其中类别和产品必须在客户服务查询中找到。
#     如果提到了一个产品，它必须与下面允许的产品列表中的正确类别关联。
#     如果没有找到产品或类别，输出一个空列表。
#     根据产品名称和产品类别与客户服务查询的相关性，列出所有相关的产品。
#     不要从产品的名称中假设任何特性或属性，如相对质量或价格。
#     允许的产品以 JSON 格式提供。
#     每个项目的键代表类别。
#     每个项目的值是该类别中的产品列表。
#     允许的产品：{products_and_category}
#     """
#     few_shot_user_1 = """我想要最贵的电脑。"""
#     few_shot_assistant_1 = """
#     [{'category': '电脑和笔记本', \
#     'products': ['TechPro 超极本', 'BlueWave 游戏本', 'PowerLite Convertible', 'TechPro
#     Desktop', 'BlueWave Chromebook']}]
#     """
#     messages = [
#         {"role": "system", "content": system_message},
#         {"role": "user", "content": f"{delimiter}{few_shot_user_1}{delimiter}"},
#         {"role": "assistant", "content": few_shot_assistant_1},
#         {"role": "user", "content": f"{delimiter}{user_input}{delimiter}"},
#     ]
#     return get_completion_from_messages(messages)


# customer_msg_0 = f"""如果我预算有限，我可以买哪款电视？"""
# products_by_category_0 = find_category_and_product_v1(
#     customer_msg_0, products_and_category
# )
# print(products_by_category_0)

# customer_msg_1 = f"""我需要一个智能手机的充电器"""
# products_by_category_1 = find_category_and_product_v1(
#     customer_msg_1, products_and_category
# )
# print(products_by_category_1)

# customer_msg_2 = f"""
# 你们有哪些电脑？"""
# products_by_category_2 = find_category_and_product_v1(
#     customer_msg_2, products_and_category
# )
# print(products_by_category_2)


# customer_msg_3 = f"""
# 告诉我关于smartx pro手机和fotosnap相机的信息，那款DSLR的。
# 我预算有限，你们有哪些性价比高的电视推荐？"""
# products_by_category_3 = find_category_and_product_v1(
#     customer_msg_3, products_and_category
# )
# print(products_by_category_3)

# customer_msg_4 = f"""
# 告诉我关于CineView电视的信息，那款8K的，还有Gamesphere游戏机，X款的。
# 我预算有限，你们有哪些电脑？"""
# products_by_category_4 = find_category_and_product_v1(customer_msg_4,products_and_category)
# print(products_by_category_4)


# def find_category_and_product_v2(user_input, products_and_category):
#     """
#     从用户输入中获取到产品和类别
#     添加：不要输出任何不符合 JSON 格式的额外文本。
#     添加了第二个示例（用于 few-shot 提示），用户询问最便宜的计算机。
#     在这两个 few-shot 示例中，显示的响应只是 JSON 格式的完整产品列表。
#     参数：
#     user_input：用户的查询
#     products_and_category：产品类型和对应产品的字典
#     """
#     delimiter = "####"
#     system_message = f"""
#     您将提供客户服务查询。\
#     客户服务查询将用{delimiter}字符分隔。
#     输出一个 Python列表，列表中的每个对象都是 JSON 对象，每个对象的格式如下：
#     '类别': <电脑和笔记本, 智能手机和配件, 电视和家庭影院系统, \
#     游戏机和配件, 音频设备, 相机和摄像机中的一个>,
#     以及
#     '名称': <必须在下面允许的产品中找到的产品列表>
#     不要输出任何不是 JSON 格式的额外文本。
#     输出请求的 JSON 后，不要写任何解释性的文本。
#     其中类别和产品必须在客户服务查询中找到。
#     如果提到了一个产品，它必须与下面允许的产品列表中的正确类别关联。
#     如果没有找到产品或类别，输出一个空列表。
#     根据产品名称和产品类别与客户服务查询的相关性，列出所有相关的产品。
#     不要从产品的名称中假设任何特性或属性，如相对质量或价格。
#     允许的产品以 JSON 格式提供。
#     每个项目的键代表类别。
#     每个项目的值是该类别中的产品列表。
#     允许的产品：{products_and_category}
#     """
#     few_shot_user_1 = """我想要最贵的电脑。你推荐哪款？"""
#     few_shot_assistant_1 = """
#     [{'category': '电脑和笔记本', \
#     'products': ['TechPro 超极本', 'BlueWave 游戏本', 'PowerLite Convertible', 'TechPro
#     Desktop', 'BlueWave Chromebook']}]
#     """
#     few_shot_user_2 = """我想要最便宜的电脑。你推荐哪款？"""
#     few_shot_assistant_2 = """
#     [{'category': '电脑和笔记本', \
#     'products': ['TechPro 超极本', 'BlueWave 游戏本', 'PowerLite Convertible', 'TechPro
#     Desktop', 'BlueWave Chromebook']}]
#     """
#     messages = [
#         {"role": "system", "content": system_message},
#         {"role": "user", "content": f"{delimiter}{few_shot_user_1}{delimiter}"},
#         {"role": "assistant", "content": few_shot_assistant_1},
#         {"role": "user", "content": f"{delimiter}{few_shot_user_2}{delimiter}"},
#         {"role": "assistant", "content": few_shot_assistant_2},
#         {"role": "user", "content": f"{delimiter}{user_input}{delimiter}"},
#     ]
#     return get_completion_from_messages(messages)


# # customer_msg_3 = f"""
# # 告诉我关于smartx pro手机和fotosnap相机的信息，那款DSLR的。
# # 另外，你们有哪些电视？"""
# # products_by_category_3 = find_category_and_product_v2(
# #     customer_msg_3, products_and_category
# # )
# # print(products_by_category_3)

# # customer_msg_0 = f"""如果我预算有限，我可以买哪款电视？"""
# # products_by_category_0 = find_category_and_product_v2(
# #     customer_msg_0, products_and_category
# # )
# # print(products_by_category_0)


# msg_ideal_pairs_set = [
#     # eg 0
#     {
#         "customer_msg": """如果我预算有限，我可以买哪种电视？""",
#         "ideal_answer": {
#             "电视和家庭影院系统": set(
#                 [
#                     "CineView 4K TV",
#                     "SoundMax Home Theater",
#                     "CineView 8K TV",
#                     "SoundMax Soundbar",
#                     "CineView OLED TV",
#                 ]
#             )
#         },
#     },
#     # eg 1
#     {
#         "customer_msg": """我需要一个智能手机的充电器""",
#         "ideal_answer": {
#             "智能手机和配件": set(
#                 ["MobiTech PowerCase", "MobiTech Wireless Charger", "SmartX EarBuds"]
#             )
#         },
#     },
#     # eg 2
#     {
#         "customer_msg": f"""你有什么样的电脑""",
#         "ideal_answer": {
#             "电脑和笔记本": set(
#                 [
#                     "TechPro 超极本",
#                     "BlueWave 游戏本",
#                     "PowerLite Convertible",
#                     "TechPro Desktop",
#                     "BlueWave Chromebook",
#                 ]
#             )
#         },
#     },
#     # eg 3
#     # {
#     #     "customer_msg": f"""告诉我关于smartx pro手机和fotosnap相机的信息，那款DSLR的。另外，你们有哪些电视？""",
#     #     "ideal_answer": {
#     #         "智能手机和配件": set(["SmartX ProPhone"]),
#     #         "相机和摄像机": set(["FotoSnap DSLR Camera"]),
#     #         "电视和家庭影院系统": set(
#     #             [
#     #                 "CineView 4K TV",
#     #                 "SoundMax Home Theater",
#     #                 "CineView 8K TV",
#     #                 "SoundMax Soundbar",
#     #                 "CineView OLED TV",
#     #             ]
#     #         ),
#     #     },
#     # },
#     # # eg 4
#     # {
#     #     "customer_msg": """告诉我关于CineView电视，那款8K电视、Gamesphere游戏机和X游戏机的信息。我的预算有限，你们有哪些电脑？""",
#     #     "ideal_answer": {
#     #         "电视和家庭影院系统": set(["CineView 8K TV"]),
#     #         "游戏机和配件": set(["GameSphere X"]),
#     #         "电脑和笔记本": set(
#     #             [
#     #                 "TechPro Ultrabook",
#     #                 "BlueWave Gaming Laptop",
#     #                 "PowerLiteConvertible",
#     #                 "TechPro Desktop",
#     #                 "BlueWave Chromebook",
#     #             ]
#     #         ),
#     #     },
#     # },
#     # eg 5
#     {
#         "customer_msg": f"""你们有哪些智能手机""",
#         "ideal_answer": {
#             "智能手机和配件": set(
#                 [
#                     "SmartX ProPhone",
#                     "MobiTech PowerCase",
#                     "SmartX MiniPhone",
#                     "MobiTech Wireless Charger",
#                     "SmartX EarBuds",
#                 ]
#             )
#         },
#     },
#     # eg 6
#     {
#         "customer_msg": f"""我预算有限。你能向我推荐一些智能手机吗？""",
#         "ideal_answer": {
#             "智能手机和配件": set(
#                 [
#                     "SmartX EarBuds",
#                     "SmartX MiniPhone",
#                     "MobiTech PowerCase",
#                     "SmartXProPhone",
#                     "MobiTech Wireless Charger",
#                 ]
#             )
#         },
#     },
#     # eg 7 # this will output a subset of the ideal answer
#     {
#         "customer_msg": f"""有哪些游戏机适合我喜欢赛车游戏的朋友？""",
#         "ideal_answer": {
#             "游戏机和配件": set(
#                 [
#                     "GameSphere X",
#                     "ProGamer Controller",
#                     "GameSphere Y",
#                     "ProGamer Racing Wheel",
#                     "GameSphere VR Headset",
#                 ]
#             )
#         },
#     },
#     # eg 8
#     {
#         "customer_msg": f"""送给我摄像师朋友什么礼物合适？""",
#         "ideal_answer": {
#             "相机和摄像机": set(
#                 [
#                     "FotoSnap DSLR Camera",
#                     "ActionCam 4K",
#                     "FotoSnap Mirrorless Camera",
#                     "ZoomMaster Camcorder",
#                     "FotoSnap Instant Camera",
#                 ]
#             )
#         },
#     },
#     # eg 9
#     {"customer_msg": f"""我想要一台热水浴缸时光机""", "ideal_answer": []},
# ]


# def eval_response_with_ideal(response, ideal, debug=False):
#     """
#     评估回复是否与理想答案匹配
#     参数：
#     response: 回复的内容
#     ideal: 理想的答案
#     debug: 是否打印调试信息
#     """
#     if debug:
#         print("回复：")
#         print(response)
#     # json.loads() 只能解析双引号，因此此处将单引号替换为双引号
#     json_like_str = response.replace("'", '"')
#     # 解析为一系列的字典
#     l_of_d = json.loads(json_like_str)
#     # 当响应为空，即没有找到任何商品时
#     if l_of_d == [] and ideal == []:
#         return 1
#     # 另外一种异常情况是，标准答案数量与回复答案数量不匹配
#     elif l_of_d == [] or ideal == []:
#         return 0
#     # 统计正确答案数量
#     correct = 0
#     if debug:
#         print("l_of_d is")
#         print(l_of_d)
#     # 对每一个问答对
#     for d in l_of_d:
#         # 获取产品和目录
#         cat = d.get("category")
#         prod_l = d.get("products")
#         # 有获取到产品和目录
#         if cat and prod_l:
#             # convert list to set for comparison
#             prod_set = set(prod_l)
#         # get ideal set of products
#         ideal_cat = ideal.get(cat)
#         if ideal_cat:
#             prod_set_ideal = set(ideal.get(cat))
#         else:
#             if debug:
#                 print(f"没有在标准答案中找到目录 {cat}")
#                 print(f"标准答案: {ideal}")
#             continue
#         if debug:
#             print("产品集合：\n", prod_set)
#             print()
#             print("标准答案的产品集合：\n", prod_set_ideal)
#         # 查找到的产品集合和标准的产品集合一致
#         if prod_set == prod_set_ideal:
#             if debug:
#                 print("正确")
#             correct += 1
#         else:
#             print("错误")
#             print(f"产品集合: {prod_set}")
#             print(f"标准的产品集合: {prod_set_ideal}")
#         if prod_set <= prod_set_ideal:
#             print("回答是标准答案的一个子集")
#         elif prod_set >= prod_set_ideal:
#             print("回答是标准答案的一个超集")
#     # 计算正确答案数
#     pc_correct = correct / len(l_of_d)
#     return pc_correct


# # print(f'用户提问: {msg_ideal_pairs_set[7]["customer_msg"]}')
# # print(f'标准答案: {msg_ideal_pairs_set[7]["ideal_answer"]}')

# # response = find_category_and_product_v2(
# #     msg_ideal_pairs_set[7]["customer_msg"], products_and_category
# # )
# # print(f"回答: {response}")
# # v = eval_response_with_ideal(response, msg_ideal_pairs_set[7]["ideal_answer"])
# # print(v)

# score_accum = 0
# for i, pair in enumerate(msg_ideal_pairs_set):
#     time.sleep(20)
#     print(f"示例 {i}")
#     customer_msg = pair['customer_msg']
#     ideal = pair['ideal_answer']
#     # print("Customer message",customer_msg)
#     # print("ideal:",ideal)
#     response = find_category_and_product_v2(customer_msg,
#     products_and_category)
#     # print("products_by_category",products_by_category)
#     score = eval_response_with_ideal(response,ideal,debug=False)
#     print(f"{i}: {score}")
#     score_accum += score
# n_examples = len(msg_ideal_pairs_set)
# fraction_correct = score_accum / n_examples
# print(f"正确比例为 {n_examples}: {fraction_correct}")


# 第十章 评估（下）——不存在简单的正确答案