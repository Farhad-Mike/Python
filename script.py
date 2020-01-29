import os

def get_string(message, name="string", default=None,
               minimum_length=0, maximum_length=80):
    message += ": " if default is None else " [{0}]: ".format(default)
    while True:
        try:
            line = input(message)
            if not line:
                if default is not None:
                    return default
                if minimum_length == 0:
                    return ""
                else:
                    raise ValueError("{0} may not be empty".format(
                                     name))
            if not (minimum_length <= len(line) <= maximum_length):
                raise ValueError("{0} must have at least {1} and "
                        "at most {2} characters".format(
                        name, minimum_length, maximum_length))
            return line
        except ValueError as err:
            print("ERROR", err)


def get_integer(message, name="integer", default=None, minimum=0,
                maximum=100, allow_zero=True):

    class RangeError(Exception): pass

    message += ": " if default is None else " [{0}]: ".format(default)
    while True:
        try:
            line = input(message)
            if not line and default is not None:
                return default
            i = int(line)
            if i == 0:
                if allow_zero:
                    return i
                else:
                    raise RangeError("{0} may not be 0".format(name))
            if not (minimum <= i <= maximum):
                raise RangeError("{0} must be between {1} and {2} "
                        "inclusive{3}".format(name, minimum, maximum,
                        (" (or 0)" if allow_zero else "")))
            return i
        except RangeError as err:
            print("ERROR", err)
        except ValueError as err:
            print("ERROR {0} must be an integer".format(name))



def get_files():
    '''Return .lst extension files from application catalog'''
    files = os.listdir()
    files = [i for i in files if i.endswith('.lst')]
    return files



def open_file(filename= ''):
    '''Create or open a new file'''
    fh = {
        'append': open(filename, 'a', encoding='utf8'),
        'read': open(filename)
    }
    return fh

def slct_file(lstFiles):
    try:
        if lstFiles:
            [print(str(int(index + 1)) + ': ', item) for index, item in enumerate(lstFiles)]
            index = int(get_string('Please select a file or create a new', default='0'))
            fileName = lstFiles[index - 1]
        if not lstFiles or index == 0:
            raise ValueError() 
    except ValueError:
        fileName = get_string('Please set file name', minimum_length=5)
        print('No items are in the list')
        return fileName
    fh = open_file(fileName)
    return fh



def main():
    lstFiles = get_files()
    information = ['[A]dd', '[D]elete', '[S]ave', '[Q]uit']
    # find or create a new file
    fh = slct_file(lstFiles)

    words = []
    for i in fh['read'].readlines():
        words.append(i.strip())
    sorted(words)
    while True:
        [print(str(int(index + 1)) + ': ', item) for index, item in enumerate(words)]
        slct = input(' '.join(information) + ':')
        slct = slct.lower()
        
        if slct == 'a':
            newItem = input('Enter: ')
            words.append(newItem)
        elif slct == 'd':
            deletItem = get_string('Select item or for exit', default='0')
            deletItem = int(deletItem)
            if not deletItem:
                return
            deletItem -= 1
            del words[deletItem]
        elif slct == 's':
            for i in words:
                i += '\n'
                if i in fh['read'].readlines():
                    continue
                fh['append'].write(i + '\n')
        elif slct == 'q':
            for i in words:
                i += '\n'
                if i in fh['read'].readlines():
                    continue
                elif i not in fh['read'].readlines():
                    approve = get_string('You have some not saved files. Do you want save them? [Y]', default='N')
                    approve = approve.lower()
                if approve == 'n':
                    return
                else:
                    for j in words:
                        j += '\n'
                        if j in fh['read'].readlines():
                            continue
                        fh['append'].write(j)
                    return






        sorted(words)
 

main()
