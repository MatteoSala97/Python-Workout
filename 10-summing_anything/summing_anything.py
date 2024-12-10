def mysum(*items):
    if not items: 
        return items
    output = items[0]
    for i in items[1:]:
        output += i  
    return output

print(mysum(10, 202, 310, 400)) #Output: 922
print(mysum('a', 'b','14', 'l')) #Output: 'ab14l'

#----------------------------------------------------------------------

def mysum_bigger_than(threshold, *items):
    filtered_items = [item for item in items if item > threshold]
    if not filtered_items:
        return filtered_items
    output = filtered_items[0]
    for i in filtered_items[1:]:
        output += i
    return output

print(mysum_bigger_than(10, 5, 20, 30, 6))  # Output: 50
print(mysum_bigger_than('m', 'a', 'b', 'n', 'o'))  # Output: 'no'

#----------------------------------------------------------------------

def sum_numeric(*items):
    total = 0
    for item in items:
        try:
            total += int(item)
        except ValueError:
            pass
    return total

print(sum_numeric(10, 20, 'a', '30', 'bcd'))  # Output: 60
print(sum_numeric('1', 2, '3.5', '4', 'xyz', 5.0))  # Output: 12

#----------------------------------------------------------------------

def combine_dicts(dict_list):
    result = {}
    for dictionary in dict_list:
        for key, value in dictionary.items():
            if key in result:
                if isinstance(result[key], list):
                    result[key].append(value)
                else:
                    result[key] = [result[key], value]
            else:
                result[key] = value
    return result

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
dict3 = {'a': 5, 'd': 6}

print(combine_dicts([dict1, dict2, dict3])) # Output: {'a': [1, 5], 'b': [2, 3], 'c': 4, 'd': 6}

