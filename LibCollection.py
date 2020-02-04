import collections

Tup = collections.namedtuple('TUP', 'x y z')
coordinate = Tup(2, 3, 4) # TUP(x=2, y=3, z=4)
coordinate = coordinate._replace(z = 5) # TUP(x=2, y=3, z=5)

dic = collections.defaultdict(func) # will return the argumented function if key not exist
collections.UserDict 
collections.UserList
collections.deque # похож на список, но обеспечивают очень быстрое добавление и удаление элементов на обоих концах очереди – как в конце, так и в начале.