#Author: antlampas
#Date: 2022-12-18
#This work is licensed under the Creative Commons Attribution 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/ or send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

import defusedxml.minidom

#TODO: review the code to use the xml.dom library in a better and optimized way

class xmlPrettifier:
    """XML Prettifier

    A XML prettyfier: it basically converts the XML format in plain text, just
    removing the XML tags.
    """
    currentDocument      = ""
    currentNode          = ""
    currenNodeAttributes = {}
    def __init__(self,document=""):
        """Constructor

        document = XML string: the XML document the Prettifier should be initialized
        """
        if document == "":
            raise Exception("No XML given")
        self.getDocument(document)
        self.getNode(self.currentDocument.firstChild.nodeName,0)
    def getDocument(self,document):
        self.currentDocument = defusedxml.minidom.parseString(document)
    def getNode(self,node,i):
        n = self.currentDocument.getElementsByTagName(node).item(i)
        if n is not None:
            self.currentNode = n
    def getNodeContent(self):
        if self.currentNode.hasChildNodes() and self.currentNode.firstChild.nodeValue is not None:
            return str(self.currentNode.firstChild.nodeValue)
        elif self.currentNode.nodeValue is not None:
            return str(self.currentNode.nodeValue)
        else:
            return None
    def prettify(self):
        """Prettify

        This makes the actual work: reads the XML document node by node and
        clears all the tags. The output format is the content of each note, one
        content per line
        """
        response = []
        if self.currentNode is not None:
            if self.currentNode.hasChildNodes():
                for node in self.currentNode.childNodes:
                    for i in range(0,len(self.currentNode.childNodes)-1):
                        self.getNode(node.nodeName,i)
                        nodeContent = self.getNodeContent()
                        if nodeContent is not None:
                            if self.currentNode.getAttribute("Prompt") == "false" and self.currentNode.getAttribute("Input") == "false":
                                response.append(nodeContent)
        return response