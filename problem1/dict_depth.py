def print_depth(data, depth=0):
    """
    :param data: dictionary
    :param depth: optional
    :return: None
    """
    for key, value in data.items():
        print(key, depth + 1)
        if isinstance(value, dict):
            print_depth(value, depth=depth + 1)


if __name__ == '__main__':
    a = {
        "key1": 1,
        "key2": {
            "key3": 1,
            "key4": {
                "key5": 4
            }
        }
    }
    print_depth(a)
