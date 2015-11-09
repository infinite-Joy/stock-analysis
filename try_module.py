def trying(tree, x_path):
    try:
        value = tree.xpath(x_path)[0]
        value = value.replace(",", "") # take into account if there are ,<comma> in numbers
        value = float(value)
    except:
        value = 0
    return value
    
def get_correct_ratio(ratio1, ratio2):
    if ratio1 > 0:
        return ratio1
    elif ratio2 > 0:
        return ratio2
    else:
        return 0