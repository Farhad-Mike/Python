import xml.dom.minidom

dom = xml.dom.minidom.parse('xml')
element = dom.getElementsByTagName('incident')
print(element[0].childNodes[0].data)
print(element[0].childNodes[0].nodeType)