def trying(tree, x_path):
    try:
        value = float(tree.xpath(x_path)[0])
    except:
        value = 0
    return value
