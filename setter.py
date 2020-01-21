setter = {'a', 'few', 'some', 'value'} # Once a set is created, you cannot change its items, but you can add new items.
setter.add('elem') # add one element
setter.update(['a', 'few', 'new', 'elements']) # add a few new elements
setter.discard('element') # don't return error if element doesn't exist
setter.remove('element') # return error if doesn't exist element
setter.pop()
setter.clear() # clear all set. Make them empty
setter.union(newSetter) # join sets
setter.update(newSetter) # join sets. Both union() and update() will exclude any duplicate items.
setter.copy() # copy 'set'
del setter # delete set
key in setter # True/False