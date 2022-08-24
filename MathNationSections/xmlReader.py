from xml.dom import minidom


class XmlReader:
    def __init__(self):
        self.document = minidom.parse('Configuration Files/test_configuration.xml')

    def test_init_data(self, data):
        item = self.document.getElementsByTagName(data)[0].firstChild.nodeValue
        return item
