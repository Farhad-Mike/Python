import xml.etree.ElementTree # Создания DOM вручную 
import xml.dom.minidom # Создание DOM при помощи методов как JS

node.nodeType

##################################### xml.etree.ElementTree #####################################
#### export ####
root = xml.etree.ElementTree.Element('rootName', attribObject/key=value) # create a tag with attributes
element = xml.etree.ElementTree.SubElement(root, 'elementName') # create a tag inside a parent tag
element.text = 'add text/delete text'
root.append(element) # add an element to parent element 
xml.etree.ElementTree.ElementTree(root) #
tree.write(filename, 'UTF-8') # create/modify a file and save in it

#### import ####
tree = xml.etree.ElementTree.parse('filename') # open xml file
elements = tree.findall('elementName') # return list of tags with that name
elements[0].get('attributeName') # get a value of a attrib
element.find('elementName') # return first finded element
element.text # get text inside element or return None


##################################### xml.dom.minidom #####################################
#### export ####
dom = xml.dom.minidom.getDOMImplementation() # Create DOM
tree = dom.createDocument(None, 'elementName', None) # create tree inside DOM. First arrgument URI пространства имен. Second arrgument имя тега корневого элемента. Therd arrgument тип документа
root = tree.documentElement # get root element of DOM
element = tree.createElement('elementName') # create a tag
element.setAttribute('attribute', 'value')
text_node = tree.createTextNode('text')
element.appendChild(text_node)

fh = open('filename', 'w', encoding='utf-8')
tree.writexml(fh, encoding='UTF-8') 

#### import ####
dom = xml.dom.minidom.parse('filename')
elements = dom.getElementsByTagName('elementName') # return list of elements
elements[0].getAttribute('attributeName')
elements[0].nodeType
elements[0].childNodes[0].data # get text from inside node