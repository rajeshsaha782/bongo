class Person(object):
    def __init__(self, first_name, last_name, father):
        self.first_name = first_name
        self.last_name = last_name
        self.father = father


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
        elif isinstance(value, Person):
            print_depth(value.__dict__, depth=depth + 1)


if __name__ == '__main__':
    person_a = Person("User", "1", None)
    person_b = Person("User", "2", person_a)
    a = {
        "key1": 1,
        "key2": {
            "key3": 1,
            "key4": {
                "key5": 4,
                "user": person_b
            }
        }
    }
    print_depth(a)
