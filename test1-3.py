def count_words(text):
    words = text.lower().split()
    word_dict = {}
    for word in words:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    return word_dict


def remove_duplicates(lst):
    return list(set(lst))


def student_scores_ops():
    scores = {}
    scores['张三'] = 85
    scores['李四'] = 92
    scores['王五'] = 78
    res1 = dict(scores)

    query = scores.get('李四')

    scores['张三'] = 90
    res2 = dict(scores)

    del scores['王五']
    res3 = dict(scores)

    return res1, query, res2, res3


def sort_dict_by_value(d):
    sorted_items = sorted(d.items(), key=lambda item: item[1])
    return dict(sorted_items)


def list_operations(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    intersection = list(set1 & set2)
    union = list(set1 | set2)
    return intersection, union


def custom_list_ops(lst):
    reversed_list = []
    for i in range(len(lst) - 1, -1, -1):
        reversed_list.append(lst[i])

    max_val = lst[0]
    min_val = lst[0]

    for num in lst:
        if num > max_val:
            max_val = num
        if num < min_val:
            min_val = num

    return reversed_list, max_val, min_val


if __name__ == '__main__':
    print("--- 题目1 ---")
    print(count_words("Hello world hello Python Python python"))

    print("--- 题目2 ---")
    print(remove_duplicates([1, 2, 2, 3, 4, 4, 5, 1, 6]))

    print("--- 题目3 ---")
    r1, q, r2, r3 = student_scores_ops()
    print(r1)
    print(q)
    print(r2)
    print(r3)

    print("--- 题目4 ---")
    print(sort_dict_by_value({'苹果': 50, '香蕉': 20, '橘子': 80, '西瓜': 35}))

    print("--- 题目5 ---")
    i_set, u_set = list_operations([1, 2, 3, 4, 5], [4, 5, 6, 7, 8])
    print(i_set)
    print(u_set)

    print("--- 题目6 ---")
    rev, max_v, min_v = custom_list_ops([23, 5, 89, 12, 45, 2])
    print(rev)
    print(max_v, min_v)