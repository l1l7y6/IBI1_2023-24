import xml.dom.minidom
import datetime
import xml.sax
import matplotlib.pyplot as plt

file_path = 'go_obo.xml'

#DOM
start_time1 = datetime.datetime.now()
DOMTree = xml.dom.minidom.parse(file_path)
collection = DOMTree.documentElement
TAG = collection.getElementsByTagName("term")
bio_dom, mole_dom, cell_dom = 0, 0, 0
for each_tag in TAG:
    namespace = each_tag.getElementsByTagName("namespace")[0].firstChild.data
    if namespace == "biological_process":
        bio_dom += 1
    elif namespace == "molecular_function":
        mole_dom += 1
    elif namespace == "cellular_component":
        cell_dom += 1
end_time1 = datetime.datetime.now()
execution_time_dom = end_time1 - start_time1

#Draw DOM outcome
plt.figure(figsize=(10, 5))
plt.bar(['Biological Process', 'Molecular Function', 'Cellular Component'], 
        [bio_dom, mole_dom, cell_dom], color='blue', label='DOM')
plt.title('Namespace Counts using DOM')
plt.xlabel('Namespace')
plt.ylabel('Count')
plt.legend()
plt.show()

#SAX
class NamespaceHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.in_term = False
        self.current_namespace = ''
        self.counts = {'biological_process': 0, 'molecular_function': 0, 'cellular_component': 0}

    def startElement(self, tag, attrs):
        if tag == 'term':
            self.in_term = True
        if tag == 'namespace':
            self.current_namespace = ''

    def characters(self, content):
        if self.in_term:
            self.current_namespace += content.strip()

    def endElement(self, tag):
        if tag == 'namespace':
            namespace = self.current_namespace
            if namespace in self.counts:
                self.counts[namespace] += 1
        if tag == 'term':
            self.in_term = False

start_time2 = datetime.datetime.now()
handler = NamespaceHandler()
parser = xml.sax.make_parser()
parser.setContentHandler(handler)
parser.parse(file_path)
end_time2 = datetime.datetime.now()
execution_time_sax = end_time2 - start_time2

#draw SAX outcome
plt.figure(figsize=(10, 5))
plt.bar(['Biological Process', 'Molecular Function', 'Cellular Component'],
        [handler.counts['biological_process'], handler.counts['molecular_function'], handler.counts['cellular_component']], color='C1', label='SAX')
plt.title('Namespace Counts using SAX')
plt.xlabel('Namespace')
plt.ylabel('Count')
plt.legend()
plt.show()

print('DOM method takes:', execution_time_dom)
print('SAX method takes:', execution_time_sax)