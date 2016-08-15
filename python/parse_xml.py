#!/usr/bin/python
import xml.dom.minidom

def traverse_children(elem, level):
    if elem.nodeType == elem.ELEMENT_NODE:
        print level, ":", (level * "    "), elem       

    i = 0 
    for sub_elem in elem.childNodes:
        level = traverse_children(sub_elem, level)
        if i == 0:
            level += 1
        i += 1
        if i == len(elem.childNodes) - 1:
            level -= 1

    return level

filename = "/Users/vvb/1.xml"
dom = xml.dom.minidom.parse(filename)
top_root = dom.getElementsByTagName("topRoot").item(0)
for elem in top_root.childNodes:
    traverse_children(elem, 0)


#formatted_xml = xml.toprettyxml()
#print formatted_xml
