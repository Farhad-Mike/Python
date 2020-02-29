import re # regexp

re.search('regexp string')
re.sub('regexp string', 'new line', obj)
pattern = re.compile('regexp string', re.IGNORECASE) # re.IGNORECASE/re.I Компилирует то что нужно искать и потом можно использовать эту переменную в re.search()
pattern.sub('new line', obj)
