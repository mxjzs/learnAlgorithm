def selectSort(array):
    """
    :param array: 要排序的数组
    :return: 排序后的数组
    """
    # 排序数组的长度
    length_array = len(array)
    # 先从数组中找出一个最小的放在下标0处，然后从剩下的元素中找到最小的，直到剩余元素为1
    temp = 0
    # temp表示每次找出的最小值要放的位置
    while temp < length_array:
        # 每轮都假设已经放在temp位置的就是要找的最小值
        minElement = array[temp]
        # 最小值的下标
        minIndex = temp
        # 然后从temp + 1 ~ 数组长度-1的位置开始依次和放在temp位置的值进行比较
        for i in range(temp + 1, length_array):
            # 如果比temp值小，那么就将最小值，最小值的下标进行更新
            if array[i] < minElement:
                # 更新最小值下标
                minIndex = i
                # 更新最小值
                minElement = array[i]
        # 查找结束后，将原本放在temp的值，更新到找到的最小值的位置
        array[minIndex] = array[temp]
        # 将temp位置的值，更新为找到的最小值
        array[temp] = minElement
        # temp指针后移，后移到还未排序的区域
        temp += 1
    return array


def test01():
    array = [5, 2, 3, 1, 7, 8, 9, 4, 6, 0]
    print("排序前数组为{}".format(array))
    print("排序后数组为{}".format(selectSort(array)))


if __name__ == "__main__":
    test01()
