def insertionSort(array):
    """
    :param array: 要排序的数组
    :return: 从小到大排序后的数组
    """
    # 获取要排序数组的长度
    length_array = len(array)
    # 如果数组长度<=1，代表不用排序，直接返回原数组
    if length_array <= 1:
        return array
    # 下标为0的是已排序了区域，其它是未排序区域，从未排序区域中依次取值和已排序的进行比较
    # 未排序区域
    for i in range(1, length_array):
        # 用一个临时变量保存取出的未排序的值
        temp = array[i]
        # 已排序区域,下标0-i-1的就是已排序区域，这里是从i-1到0变量
        j = i - 1
        # 如果temp < array[j]，array[j]的值就要移到arr[j + 1]处，否则temp的值就移到arr[j+1]处
        while j >= 0 and temp < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = temp
    return array


def test01():
    array = [2, 5, 4, 1, 3]
    print("排序前的数组{}".format(array))
    insertionSort(array)
    print("排序后的数组{}".format(array))


if __name__ == "__main__":
    test01()
