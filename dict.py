dictionary = {}
dict.pop()
{key: value for key, value in iterable if condition}
dictionary.items() # выводит список множеств (ключ, значение)
dictionary.get('key', 0) # есть есть ключ то верни его значение, если его нет то верни 0

dictionary = collections.defaultdict(func) # вызовет эту функцию при обращении к несуществующему ключю