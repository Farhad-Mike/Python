list(str) # create list from string
[expression for item in iterable]
[expression for item in iterable if condition]
arr = [_ * 2 for _ in ‘spam’] # Дублирование символов в строке  [‘ss’, ‘pp’, ‘aa’, ‘mm’]
arr = [M[i][i] for i in [0, 1, 2]] # Выборка элементов диагонали матрицы
arr = [row[2] for row in arr] # create new array and add to them from all multidimensional arrays indexed elem
arr = [row[2] for row in arr if condition] #if condition return true then return elem
arr = [c + d for c in 'list' if c != 'i'  for d in 'spam' if d != 'a'] # ['ls', 'lp', 'lm', 'ss', 'sp', 'sm', 'ts', 'tp', 'tm']
arr.append(value) #like arr.push(); but can add only 1 value
list.append(arr, value) # second variant like arr.push()
arr.extend(arr2) # like arr.push(...arr2)
arr.pop()
arr.insert(position, newElem) #add new elem to the position
arr.remove(value) #find and delete the value
arr.sort()
arr.reverse()
arr.copy() # will copy list
arr * 3 #repeat inner elements a few times
arr + arr2
'value' in arr # does array contain the value. Return True or False
'value' not in arr # does array not contain the value. if not exist then return True
arr += 'str' # add like [s, t, r]
arr += ['str'] # add like ['str']
del arr # delete list
del arr[0] # delete index
arr.clear() # empties list
arr.index('element') # return index of first founded element