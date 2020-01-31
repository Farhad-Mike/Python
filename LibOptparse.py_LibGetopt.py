import optparse
import getopt
# Оба модуля для работы с передаваемыми параметрами в командной строке.

parser = optparse.OptionParser()
parser.add_option('-w', '--maxwidth', dest='maxwidth', type='int', help='you should input integer [default: "%default"]') # аргумент help выступает как строка при использовании команды -h --help
parser.add_option("-f", "--format", dest="format", help=("the format used for outputting numbers " "[default: %default]"))
parse.set_defaults(maxwidth=100, format=".0f") 
opts, args = parse.parse_args() # в opts запишутся основные значения, в args Все аргументы командной строки, которые не были обработаны.