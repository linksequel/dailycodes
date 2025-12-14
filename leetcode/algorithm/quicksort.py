def quicksort(arr):
    """
    快速排序算法实现

    Args:
        arr: 待排序的列表

    Returns:
        排序后的列表
    """
    # 基本情况：如果数组长度小于等于1，则已经有序
    if len(arr) <= 1:
        return arr

    # 选择基准元素（这里选择中间元素）
    pivot = arr[len(arr) // 2]

    # 分割数组为三部分：小于基准、等于基准、大于基准
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    # 递归排序并合并结果
    return quicksort(left) + middle + quicksort(right)


def quicksort_inplace(arr, low=0, high=None):
    """
    原地快速排序算法实现

    Args:
        arr: 待排序的列表
        low: 排序范围的起始索引
        high: 排序范围的结束索引
    """
    if high is None:
        high = len(arr) - 1

    if low < high:
        # 分区操作，返回基准元素的正确位置
        pivot_index = partition(arr, low, high)

        # 递归排序基准左边和右边的子数组
        quicksort_inplace(arr, low, pivot_index - 1)
        quicksort_inplace(arr, pivot_index + 1, high)


def partition(arr, low, high):
    """
    分区函数，将数组分为两部分

    Args:
        arr: 数组
        low: 起始索引
        high: 结束索引

    Returns:
        基准元素的最终位置
    """
    # 选择最后一个元素作为基准
    pivot = arr[high]

    # 较小元素的索引
    i = low - 1

    for j in range(low, high):
        # 如果当前元素小于或等于基准
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # 将基准放到正确位置
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# 测试代码
if __name__ == "__main__":
    # 测试非原地排序版本
    test_arr1 = [64, 34, 25, 12, 22, 11, 90]
    print("原始数组:", test_arr1)
    # sorted_arr1 = quicksort(test_arr1)
    # print("排序后数组:", sorted_arr1)

    # 测试原地排序版本
    # test_arr2 = [64, 34, 25, 12, 22, 11, 90]
    test_arr2 = [15, 18, 20, 12, 17]
    print("\n原始数组:", test_arr2)
    quicksort_inplace(test_arr2)
    print("原地排序后:", test_arr2)