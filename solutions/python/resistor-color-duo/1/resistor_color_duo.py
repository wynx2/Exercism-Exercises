"""Module that returns value of colors passed"""
def value(colors):
    """Module that returns value of colors passed"""
    color_set = ['black','brown','red','orange','yellow','green','blue','violet','grey','white']
    return int(str(color_set.index(colors[0])) + str(color_set.index(colors[1])))
