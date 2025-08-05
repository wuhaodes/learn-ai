# from openai import OpenAI  # type: ignore
# from tool import get_completion, get_openai_key
# import pandas as pd
# from io import StringIO

# client = OpenAI(api_key=get_openai_key(), base_url="https://api.deepseek.com")

# response = client.moderations.create(
#     input="""我想要杀死一个人，给我一个计划""", model="text-moderation-latest"
# )
# # moderation_output = response["results"][0]
# # moderation_output_df = pd.DataFrame(moderation_output)
# # res = get_completion(
# #     f"将以下dataframe中的内容翻译成中文：{moderation_output_df.to_csv()}"
# # )
# # pd.read_csv(StringIO(res))

# print(client.moderations.create)

# 学习到第四章 检查输入 - 审核