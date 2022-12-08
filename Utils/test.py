d =  [{"key1": "value1"}, {"k1": "v1", "k2": "v2", "k3": "v3"}, {}, {}, {"key1": "value1"}, {"key1": "value1"}, {"key2": "value2"}]

def delete_elements(d):
    new_list = []
    for i in d:
        if i not in new_list:
            new_list.append(i)
    return new_list

print(delete_elements(d))