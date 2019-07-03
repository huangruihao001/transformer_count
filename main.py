def p2p_distance(p1,p2):
    """
    计算两点之间的直线距离
    :param p1: 点1列表坐标，如[0,0,0]
    :param p2: 点2列表坐标，如[10,10,10]
    :return: p1和p2两点之间的直线距离
    """
    distance = ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2) ** 0.5
    return distance

def transformer_count_sub(light, min_distance, voltage):
    """
    计算所需变压其数量
    :param light: 灯的位置参数列表，如light = [[0,0,0,5], [10,10,10,5],]
    :param min_distance: 灯与灯之间允许的最大距离
    :param voltage: 变压器的额定电压
    :return: 变压器数量
    """
    i = 0
    j = 0
    unit_voltage = light[0][3]
    while (j < (len(light)-1)) and (len(light) > 1):
        print(light[0])
        print(light[i+1])
        distance = p2p_distance(light[0], light[i+1])
        print(distance)
        if distance <= min_distance and unit_voltage <= voltage:
            unit_voltage += light[i+1][3]
            del light[i+1]
        else:
            i += 1
        j += 1
    print(light)
    print(len(light))
    del light[0]
    return light

def transformer_count(sub,light, min_distance, voltage):
    if len(light) > 1:
        i = 0
        while i < (len(light)-1):
            light = transformer_count_sub(sub, light, min_distance, voltage)



if __name__ == '__main__':

    light = [[0,0,0,5],
             [10,10,10,5],
             [20,20,20,5],
             [200,200,200,5],
             [210,210,210,5],
             [220,220,220,5]]
    # p1 = [0,0,0]
    # p2 = [10,10,10]
    # a = p2p_distance(p1, p2)
    # print(a)
    transformer_count(light, 80, 16)
