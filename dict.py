import collections

dictionary = {}
dict.pop()
{key: value for key, value in iterable if condition}
dictionary.items() # выводит список множеств (ключ, значение)
dictionary.keys() # return keys
dictionary.values() # return key's value
dictionary.copy() # copy 'dict'

dictionary[somekey] = dictionary.get('key', 0) # есть есть ключ то верни его значение, если его нет то запиши туда 0

dictionary = collections.defaultdict(func) # вызовет эту функцию при обращении к несуществующему ключю

defdict = collections.defaultdict(str) # return '' when called not existed key. You can use any default object type func (example: str, int, dict, float and s.)