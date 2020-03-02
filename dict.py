import collections

dictionary = {}
dictionary = {one = 1, **otherDict}
dict.pop()
{key: value for key, value in iterable if condition}
dictionary.items() # выводит список множеств (ключ, значение)
dictionary.keys() # return keys
dictionary.values() # return key's value
dictionary.copy() # copy 'dict'
dict.pop(key[, default]) # Возвращает значение по указанному ключу и убирает элемент из словаря. default : Значение, которое следует вернуть, если указанный ключ отсутствует в словаре. Если не указано, при отсутствии ключа возбуждается исключение KeyError

dictionary[somekey] = dictionary.get('key', 0) # есть есть ключ то верни его значение, если его нет то запиши туда 0

dictionary = collections.defaultdict(func) # вызовет эту функцию при обращении к несуществующему ключю

defdict = collections.defaultdict(str) # return '' when called not existed key. You can use any default object type func (example: str, int, dict, float and s.)
dict.update()
dict.fromkeys() # Этот метод используется для создания нового словаря на основе итерируемого объекта. Каждый элемент итерируемого объекта становится ключом, а значением каждого ключа становится None или значение аргумента value.
dict.popitem() # удаляет и возвращает случайный элемент ключзначение из словаря.
dict.setdefault() # возвращает значение для заданного ключа или, если элемента с таким ключом нет, создает новый элемент с заданным ключом и значением и возвращает значение