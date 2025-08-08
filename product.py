from json_tool import get_json_str

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
