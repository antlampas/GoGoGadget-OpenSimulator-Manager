#Author: Red Erik @ OSGrid
#Date: 2022-12-18
#This work is licensed under the Creative Commons Attribution 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/ or send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

import defusedxml.minidom

class xmlPrettifier:
    currentDocument=""
    currentNode=""
    currenNodeAttributes={}
    def __init__(self,document=""):
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
        response = ""
        if self.currentNode is not None:
            if self.currentNode.hasChildNodes():
                for node in self.currentNode.childNodes:
                    for i in range(0,len(self.currentNode.childNodes)-1):
                        self.getNode(node.nodeName,i)
                        nodeContent = self.getNodeContent()
                        if nodeContent is not None:
                            if self.currentNode.getAttribute("Prompt") == "false" and self.currentNode.getAttribute("Input") == "false":
                                response += nodeContent + "\n"
        return response