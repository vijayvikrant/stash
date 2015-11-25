#!/usr/bin/env python

# usage ./check_rns.py <schema_ref> <schema_diff>
import sys
import xml.etree.ElementTree

if len(sys.argv) < 3:
    print "usage ./check_rns.py <schema_ref> <schema_diff>"
    sys.exit(0)


ns = "{http://www.w3.org/2001/XMLSchema}"


def form_xpath(elem_type, name, value):
    ns = "{http://www.w3.org/2001/XMLSchema}"
    xpath = './/' + ns + elem_type + '[@' + name + '="' + value + '"]'
    return str(xpath)


def make_rn_dict(filename):
    rn_dict = {}
    e = xml.etree.ElementTree.parse(filename).getroot()
    xpath = form_xpath('element', 'substitutionGroup', 'managedObject')
    for each in e.findall(xpath):
        key = each.attrib['name']
        node = e.find(form_xpath('complexType', 'name', key))
        if node is None:
            continue
        for _ in list(node[0][0]):
            if _.tag == 'rn':
                rn = _.attrib['value']
                rn_dict[key] = rn
                break
    return rn_dict

dict_src = make_rn_dict(sys.argv[1])
dict_dst = make_rn_dict(sys.argv[2])
for each in dict_src:
    if each not in dict_dst:
        continue
    if dict_src[each] != dict_dst[each]:
        print "Mo: " + each + " Prev:" + dict_src[each] + " New:" + dict_dst[each]
