"""
冒泡排序：从头到尾，两个相邻的依次比较，每次比较找出一个最值
"""


def bubbleSort(array):
    """
    冒泡排序，从小到大
    :param array: 要排序的数组
    :return: 从小到大排序后的数组
    """
    # 获取要排序数组的长度
    length_array = len(array)
    # 如果数组长度<=1，代表不用排序，直接返回原数组
    if length_array <= 1:
        return array
    # 每一轮找出一个最值，n个元素需要n-1次
    for i in range(length_array - 1):
        # 每一轮找出一个元素后，下一轮就可以少比较一次
        for j in range(1, length_array - i):
            # 比较两个相邻的值，大（左边）的和小（右边）的交换位子
            if array[j - 1] > array[j]:
                temp = array[j]
                array[j] = array[j - 1]
                array[j - 1] = temp
    return array


def test01():
    array1 = [5, 4, 3, 2, 1, 0]
    array2 = [1, 2, 3, 4, 5, 6, 7]
    array3 = [2, 3, 9, 7, 1, 4, 6, 8]
    array4 = []
    array5 = [5, 4, 9, 5, 8, 1, 2, 4, 3, 6, 7]
    list = [array1, array2, array3, array4, array5]
    for i in list:
        print("排序前的数组:", i)
        print("排序后的数组:", bubbleSort(i))
        print()


if __name__ == "__main__":
    test01()
