"""
二分查找前提：数据是有序的
"""


def binarySearch(array, element):
    """
    二分查找
    :param array: 已排序好的数组，这样假定为升序
    :param element: 要查找的元素
    :return: element在数组中的下标，没在就返回-1
    """
    # 数组长度
    length_array = len(array)
    # 如果数组长度为0，代表数组为空，直接返回-1
    if length_array == 0:
        return -1
    # 二分查找，是将区间一分为2进行查找
    # 左区间,初始值为0
    left = 0
    # 右区间，初始值为数组长度-1
    right = length_array - 1
    # 右区间最大值小于要找的值 or 左区间最小的值小于要找的值，表示element不在数组中
    if array[right] < element or array[left] > element:
        return -1
    while right - left > 1:
        # 左右区间的中间
        k = (left + right) // 2
        # 如果中间的值比要找的值大，那么右区间就要移到K
        if array[k] > element:
            right = k
        # 如果中间的值比要找的值小，那么左区间就要移到K
        elif array[k] < element:
            left = k
        else:
            return k
    # 当right - left <= 1时
    if array[left] == element:
        return left
    if array[right] == element:
        return right
    return -1


def test01():
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("要查找的目标数组:")
    print("{}".format(array))
    for i in range(11):
        print("要查找的数为：{}".format(i), end="\t")
        print("返回查找的下标：{}".format(binarySearch(array, i)))


if __name__ == "__main__":
    test01()
