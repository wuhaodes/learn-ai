# from tool import get_completion_from_messages
from json_tool import read_string_to_list
from product import generate_output_string

# 二、检索详细信息

# product = get_product_by_name("TechPro Ultrabook")
# print(product)

# category_products = get_products_by_category("电脑和笔记本")
# print(category_products)

# json_str = '{"Billing": ["Unsubscribe or upgrade", "Add a payment method", "Explanation for charge", "Dispute a charge"], "Technical Support": ["General troubleshooting", "Device compatibility", "Software updates"], "Account Management": ["Password reset", "Update personal information", "Close account", "Account security"], "General Inquiry": ["Product information", "Pricing", "Feedback", "Speak to a human"]}'
# list = read_string_to_list(json_str)
# print(list)

# 3.2 进行检索

str = """
[{'category': 'Smartphones and Accessories', 'products': ['SmartX ProPhone']},
{'category': 'Cameras and Camcorders', 'products': ['FotoSnap DSLR Camera',
'FotoSnap Mirrorless Camera', 'FotoSnap Instant Camera']}, {'category':'Televisions and Home Theater Systems', 'products': ['CineView 4K TV', 'CineView 8K TV', 'CineView OLED TV', 'SoundMax Home Theater', 'SoundMax Soundbar']}]
"""

category_product_list = read_string_to_list(str)
# print(category_product_list)

product_information_for_user_message_1 = generate_output_string(category_product_list)
print(product_information_for_user_message_1)


# 3.3 生成用户查询的答案