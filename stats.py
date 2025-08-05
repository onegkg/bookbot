def count_words(words):
    return len(words.split())


def char_count(words):
    if not isinstance(words, str):
        raise Exception("char_count only supports operations on strings")
    letter_dict = dict()
    for char in words:
        lower = char.lower()
        letter_dict[lower] = letter_dict.get(lower, 0) + 1
    return letter_dict


def sort_on(items):
    return items["num"]


def smooth_dict(input_dict):
    dict_list = []
    for k, v in input_dict.items():
        dict_list.append({"char": k, "num": v})
    dict_list.sort(key=sort_on, reverse=True)
    return dict_list
