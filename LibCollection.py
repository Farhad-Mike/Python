import collections

tup = collections.namedtuple('Name', 'index00Name index01Name index02Name')
variable2 = tup('index00', 'index01', 'index02') # Name(index00Name= index00, index01Name= index01, index02Name=index02)
variable2.index00Name # index00