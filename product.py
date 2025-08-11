from json_tool import get_json_str, json_dumps

products = get_json_str("products_zh.json")


def get_product_by_name(name):
    """
    根据产品名称获取产品
    参数:
    name: 产品名称
    """
    return products.get(name, None)


def get_products_by_category(category):
    """
    根据类别获取产品
    参数:
    category: 产品类别
    """
    return [product for product in products.values() if product["类别"] == category]


def get_all_products(products_list):
    output_string = ""
    for product_name in products_list:
        product = get_product_by_name(product_name)
        if product:
            output_string += json_dumps(product, indent=4, ensure_ascii=False) + "\n"
        else:
            print(f"Error: Product '{product_name}' not found")
    return output_string


def get_all_category_products(category_name):
    category_products = get_products_by_category(category_name)
    output_string = ""
    for product in category_products:
        output_string += json_dumps(product, indent=4, ensure_ascii=False) + "\n"
    return output_string


def generate_output_string(data_list):
    """
    根据输入的数据列表生成包含产品或类别信息的字符串。
    参数:
    data_list: 包含字典的列表，每个字典都应包含 "products" 或 "category" 的键。
    返回:
    output_string: 包含产品或类别信息的字符串。
    """
    output_string = ""
    if data_list is None:
        return output_string

    for data in data_list:
        try:
            if "products" in data and data["products"]:
                output_string += get_all_products(data["products"])
            elif "category" in data and data["category"]:
                output_string += get_all_category_products(data["category"])
            else:
                print("Error: Invalid object format")
        except Exception as e:
            print(f"Error: {e} {data}")

    return output_string
